from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from collections import OrderedDict
from saiki.utils import get_course_color
from course.models import CourseOffering, CourseEnrollment
from .serializers import CourseOfferingSerializer, CourseEnrollmentSerializer

class StudentCourseList(APIView):
    
    def get(self, request, st_pk):
        queryset = CourseOffering.objects.filter(courseenrollment__student_id=st_pk)
        data = []

        for course in queryset:
            color = get_course_color(course.course.code)
            d = OrderedDict()
            d['id'] = course.pk
            d['slug'] = course.slug
            d['description'] = course.course.description
            d['term'] = str(course.term)
            d['code'] = course.course.code
            ce = course.courseenrollment_set.get(student_id=st_pk)
            d['request_url'] = reverse('course_api:course_enrollment_detail', kwargs={'c_pk': course.pk, 'ce_pk': ce.pk})
            d['is_hidden'] = ce.is_hidden
            d['href'] = reverse('course:detail', kwargs={'slug': course.slug})
            d['color_bg'] = color[0]
            d['color_fg'] = color[1]
            
            data.append(d)

        return Response(data)

class TeacherCourseList(APIView):
    def get(self, request, teacher_pk):
        queryset = CourseOffering.objects.filter(teacher_id=teacher_pk)
        data = []

        for course in queryset:
            color = get_course_color(course.course.code)

            d = OrderedDict()
            d['id'] = course.pk
            d['slug'] = course.slug
            d['description'] = course.course.description
            d['term'] = str(course.term)
            d['code'] = course.course.code
            d['request_url'] = reverse('course_api:course_detail', kwargs={'c_pk': course.pk})
            d['is_hidden'] = course.archive
            d['href'] = reverse('course:detail', kwargs={'slug': course.slug})
            d['color_bg'] = color[0]
            d['color_fg'] = color[1]
            
            data.append(d)

        return Response(data)

class CourseOfferingDetail(generics.RetrieveUpdateAPIView):
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer
    lookup_url_kwarg = 'c_pk'

class CourseEnrollmentList(generics.ListAPIView):
    def get_queryset(self):
        queryset = CourseEnrollment.objects.filter(course_offered_id=self.kwargs['c_pk'])

        return queryset
    # queryset = CourseEnrollment.objects.all()
    # lookup_url_kwarg = 'c_pk'
    # lookup_kwarg = 'course_offered_pk'
    serializer_class = CourseEnrollmentSerializer

class CourseEnrollmentDetail(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        return CourseEnrollment.objects.filter(course_offered_id=self.kwargs['c_pk'])
    serializer_class = CourseEnrollmentSerializer
    lookup_url_kwarg = 'ce_pk'
