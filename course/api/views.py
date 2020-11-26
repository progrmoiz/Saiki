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

class CourseOfferingList(APIView):
    
    def get(self, request, st_pk):
        queryset = CourseOffering.objects.filter(courseenrollment__student_id=st_pk)
        data = []

        for course in queryset:
            color = get_course_color(course.course.code)
            d = OrderedDict()
            d['id'] = course.pk
            d['slug'] = course.slug
            d['archive'] = course.archive
            d['description'] = course.course.description
            d['term'] = str(course.term)
            d['code'] = course.course.code
            ce = course.courseenrollment_set.get(student_id=st_pk)
            d['course-enrollment-url'] = reverse('api:course_enrollment_detail', kwargs={'c_pk': course.pk, 'ce_pk': ce.pk})
            d['is_hidden'] = ce.is_hidden
            d['href'] = reverse('course:detail', kwargs={'slug': course.slug})
            d['color_bg'] = color[0]
            d['color_fg'] = color[1]
            
            data.append(d)

        return Response(data)

class CourseOfferingDetail(generics.RetrieveUpdateAPIView):
    def get(self, request, c_pk):
        queryset = CourseOffering.objects.filter(id=c_pk)
        data = []

        for course in queryset:
            d = OrderedDict()
            d['id'] = course.pk
            d['slug'] = course.slug
            d['archive'] = course.archive
            d['description'] = course.course.description
            d['term'] = str(course.term)
            d['code'] = course.course.code
            data.append(d)

        return Response(data)
    
    def get_queryset(self):
        queryset = CourseOffering.objects.filter()

        return queryset
    serializer_class = CourseOfferingSerializer
    lookup_url_kwarg = 'c_pk'

class CourseEnrollmentList(generics.ListAPIView):
    def get_queryset(self):
        queryset = CourseEnrollment.objects.filter(course_offered_id=self.kwargs['c_pk'])

        return queryset
    serializer_class = CourseEnrollmentSerializer

class CourseEnrollmentDetail(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        return CourseEnrollment.objects.filter(course_offered_id=self.kwargs['c_pk'])
    serializer_class = CourseEnrollmentSerializer
    lookup_url_kwarg = 'ce_pk'
