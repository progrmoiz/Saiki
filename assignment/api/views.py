from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from collections import OrderedDict
from saiki.utils import get_course_color
from assignment.models import Assignment, AssignmentWork, AssignmentFile, AssignmentWorkFile
from .serializers import AssignmentSerializer, AssignmentWorkSerializer, AssignmentFileSerializer, AssignmentWorkFileSerializer
from rest_framework.reverse import reverse
from rest_framework import status

class AssignmentWorkDetail(generics.RetrieveUpdateAPIView):
    
    def get(self, request, assignmentwork_pk):
        queryset = AssignmentWork.objects.filter(pk=assignmentwork_pk)
        d = OrderedDict()

        for a in queryset:
            d['id'] = a.pk
            d['submit_date'] = a.submit_date
            d['submitted'] = a.submitted
            d['points'] = a.points
            d['assignment'] = a.assignment
            d['student'] = a.student
            d['title'] = a.assignment.title
            d['deadline'] = a.assignment.deadline
            d['description'] = a.assignment.description
            d['course_offering'] = a.assignment.course_offering.pk

            materials = AssignmentFile.objects.filter(assignment=a.assignment)
            d['materials'] = [m.file for m in materials]

            work_materials = AssignmentWorkFile.objects.filter(assignment_work=a)
            print(work_materials)
            d['work_material_urls'] = [
                reverse('assignment_api:assignment_work_file_detail', kwargs={'assignmentwork_pk': a.pk, 'workmaterial_pk': m.pk}) for m in work_materials]

        serializer = AssignmentWorkSerializer(d)

        return Response(serializer.data)
    
    queryset = AssignmentWork.objects.all()
    serializer_class = AssignmentWorkSerializer
    lookup_url_kwarg = 'assignmentwork_pk'

class AssignmentWorkFileList(generics.ListCreateAPIView):
    serializer_class = AssignmentWorkFileSerializer
    page_size = 100

    def get(self, request, assignmentwork_pk):
        queryset = AssignmentWorkFile.objects.filter(assignment_work_id=assignmentwork_pk)
        data = []

        for a in queryset:
            d = OrderedDict()
            
            d['id'] = a.pk
            d['file'] = a.file
            d['assignment_work'] = a.assignment_work
            d['request_url'] = reverse('assignment_api:assignment_work_file_detail', kwargs={'assignmentwork_pk': a.assignment_work.pk, 'workmaterial_pk': a.pk})

            data.append(d)

        serializer = AssignmentWorkFileSerializer(data, many=True)

        return Response(serializer.data)


    def get_queryset(self):
        queryset = AssignmentWorkFile.objects.filter(assignment_work_id=self.kwargs['assignmentwork_pk'])
        return queryset


class AssignmentWorkFileDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AssignmentWorkFileSerializer
    lookup_url_kwarg = 'workmaterial_pk'

    def get(self, request, assignmentwork_pk, workmaterial_pk):
        queryset = AssignmentWorkFile.objects.filter(id=workmaterial_pk)
        d = OrderedDict()

        for a in queryset:

            d['id'] = a.pk
            d['file'] = a.file
            d['assignment_work'] = a.assignment_work
            d['request_url'] = reverse('assignment_api:assignment_work_file_detail', kwargs={'assignmentwork_pk': a.assignment_work.pk, 'workmaterial_pk': a.pk})

        serializer = AssignmentWorkFileSerializer(d)

        return Response(serializer.data)

    def get_queryset(self):
        queryset = AssignmentWorkFile.objects.filter(assignment_work_id=self.kwargs['assignmentwork_pk'])
        return queryset

class AssignmentFileList(generics.ListCreateAPIView):
    serializer_class = AssignmentFileSerializer
    page_size = 100

    def get(self, request, assignment_pk):
        queryset = AssignmentFile.objects.filter(assignment_id=assignment_pk)
        data = []

        for a in queryset:
            d = OrderedDict()
            
            d['id'] = a.pk
            d['file'] = a.file
            d['assignment'] = a.assignment
            d['request_url'] = reverse('assignment_api:assignment_file_detail', kwargs={'assignment_pk': a.assignment.pk, 'material_pk': a.pk})

            data.append(d)

        serializer = AssignmentFileSerializer(data, many=True)

        return Response(serializer.data)


    def get_queryset(self):
        queryset = AssignmentFile.objects.filter(assignment_id=self.kwargs['assignment_pk'])
        return queryset

class AssignmentFileDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AssignmentFileSerializer
    lookup_url_kwarg = 'material_pk'

    def get(self, request, assignment_pk, material_pk):
        queryset = AssignmentFile.objects.filter(id=material_pk)
        d = OrderedDict()

        for a in queryset:

            d['id'] = a.pk
            d['file'] = a.file
            d['assignment'] = a.assignment
            d['request_url'] = reverse('assignment_api:assignment_file_detail', kwargs={'assignment_pk': a.assignment.pk, 'material_pk': a.pk})

        serializer = AssignmentFileSerializer(d)

        return Response(serializer.data)

    def get_queryset(self):
        queryset = AssignmentFile.objects.filter(assignment_id=self.kwargs['assignment_pk'])
        return queryset