from course.models import CourseOffering, CourseEnrollment
from rest_framework import serializers


        
class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

class CourseOfferingSerializer(serializers.ModelSerializer):
    # courseenrollment_set = CourseEnrollmentSerializer(many=True, required=False)

    class Meta:
        model = CourseOffering
        fields = '__all__'
        # lookup_field = 'slug'
