import os.path
from collections import OrderedDict

from django.shortcuts import get_object_or_404
from resources.models import ResourceFile, ResourceFolder
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .serializers import ResourceFolderSerializer, ResourceFileSerializer
import mimetypes
mimetypes.init()

class ResourceFileList(APIView):
    
    def recursive_folder(self, root_slug, parent_slug, data):
        root = ResourceFolder.objects.get(slug=root_slug)
        files = ResourceFile.objects.filter(folder__slug=root_slug)
        folders = ResourceFolder.objects.filter(parent__slug=root_slug)

        # add the root folder
        d = OrderedDict()
        d['pk'] = root.pk
        d['id'] = root_slug
        d['name'] = root.name
        d['user'] = root.user.pk
        d['isDir'] = True
        d['modDate'] = root.modified
        d['childrenIds'] = []
        d['childrenCount'] = 0

        if parent_slug:
            d['parentId'] = parent_slug
            d['request_url'] = reverse('resources_api:folder_detail', kwargs={'pk': root.pk })
            
            data[f'{parent_slug}']['childrenIds'].append(root.slug)
            data[f'{parent_slug}']['childrenCount'] += 1

        data[f'{root_slug}'] = d
        
        # recursively call this for child folder
        for f in folders:
            self.recursive_folder(f.slug, root_slug, data)

        for f in files:
            d_file = OrderedDict()
            d_file['id'] = f.slug
            d_file['name'] = f.name
            d_file['user'] = f.user.pk
            d_file['url'] = f.file.url
            d_file['size'] = f.file.size
            d_file['isHidden'] = False # intentionally set all the false
            d_file['isDir'] = False
            d_file['parentId'] = root_slug
            d_file['modDate'] = f.modified
            mimestart = mimetypes.guess_type(f.name)[0]
            if mimestart != None:
                mimestart = mimestart.split('/')[0]

                if mimestart == 'image':
                    d_file['thumbnailUrl'] = f.file.url
            d_file['request_url'] = reverse('resources_api:file_detail', kwargs={'pk': f.pk })

            # add this id to the parent children
            d['childrenIds'].append(f.slug)
            d['childrenCount'] += 1
            data[f'{f.slug}'] = d_file


        return data

    def get(self, request, folder_slug):
        queryset = ResourceFolder.objects.filter(slug=folder_slug)
        folders = ResourceFolder.objects.filter(parent__slug=folder_slug)
        files = ResourceFile.objects.filter(folder__slug=folder_slug)

        data = OrderedDict()
        data['rootFolderId'] = folder_slug
        d = self.recursive_folder(folder_slug, None, {})
        data['fileMap'] = d
        
        return Response(data)

class ResourceFileDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResourceFileSerializer
    queryset = ResourceFile.objects.all()

class ResourceFolderDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResourceFolderSerializer
    queryset = ResourceFolder.objects.all()

class ResourceFolderCreate(generics.CreateAPIView):
    serializer_class = ResourceFolderSerializer
    queryset = ResourceFolder.objects.all()

class ResourceFileCreate(generics.CreateAPIView):
    serializer_class = ResourceFileSerializer
    queryset = ResourceFile.objects.all()