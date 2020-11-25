from django.urls import include, path
from .views import CourseOfferingList, CourseOfferingDetail, CourseEnrollmentDetail, CourseEnrollmentList

app_name = 'course'
urlpatterns = [
    path("students/<int:st_pk>/", CourseOfferingList.as_view(), name="student_course_list"),
    path("courses/<int:c_pk>/", CourseOfferingDetail.as_view(), name="course_detail"),
    path("courses/<int:c_pk>/course-enrollments/", CourseEnrollmentList.as_view(), name="course_enrollment_list"),
    path("courses/<int:c_pk>/course-enrollments/<int:ce_pk>/", CourseEnrollmentDetail.as_view(), name="course_enrollment_detail"),
]

