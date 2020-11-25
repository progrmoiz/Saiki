from .models import CourseOffering, CourseEnrollment
from rest_framework import serializers


class CourseOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOffering
        fields = ['term', 'course', 'teacher', 'slug', 'archive']
        lookup_field = 'slug'
        
        
class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = []