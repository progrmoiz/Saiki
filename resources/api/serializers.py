from resources.models import ResourceFolder, ResourceFile
from rest_framework import serializers

class ResourceFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFolder
        fields = '__all__'

class ResourceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFile
        fields = '__all__'
