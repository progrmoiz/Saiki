from assignment.models import Assignment, AssignmentFile, AssignmentWork, AssignmentWorkFile
from rest_framework import serializers

        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentWorkSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256, read_only=True)
    deadline = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(max_length=256, read_only=True, required=False)
    course_offering = serializers.IntegerField(read_only=True)
    materials = serializers.ListField(child=serializers.FileField(required=False), read_only=True)
    work_material_urls = serializers.ListField(child=serializers.URLField(required=False), read_only=True)

    class Meta:
        model = AssignmentWork
        fields = '__all__'
        read_only_fields = ('points', 'student', 'assignment')

class AssignmentFileSerializer(serializers.ModelSerializer):
    request_url = serializers.URLField(required=False, read_only=True)
    
    class Meta:
        model = AssignmentFile
        fields = '__all__'

class AssignmentWorkFileSerializer(serializers.ModelSerializer):
    request_url = serializers.URLField(required=False, read_only=True)
    
    class Meta:
        model = AssignmentWorkFile
        fields = '__all__'
