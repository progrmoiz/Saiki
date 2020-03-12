import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saiki.settings')

import django
django.setup()

import random

from accounts.models import User, PrevAcademicRecord, Guardian, Teacher, Student
from course.models import Course, CourseOffering, CourseEnrollment
from university.models import University, Department, Term

from faker import Faker
fake = Faker()

# TODO: Add loging for each steps
# TODO: Add add each section to methods
# TODO: Ask user it will delete all your previous data
# TODO: Create superuser
# University.objects.all().delete()
# Department.objects.all().delete()
# Term.objects.all().delete()

# u = University(name='Harvard University')
# u.save()

# departments_ = []
# departments = [
#     ('BSCS', 'Bachelor of Science in Computer Science'),
#     ('BBA', 'Bachelor of Business Administration')
# ]

# for (c, d) in departments:
#     d, created = Department.objects.get_or_create(code=c, description=d, university=u)
#     departments_.append(d)


# terms_ = []
# terms = [
#     (2, 2020),
#     (1, 2020),
#     (2, 2019),
#     (1, 2019),
#     (2, 2018),
#     (1, 2018)
# ]

# for (h, y) in terms:
#     t, created = Term.objects.get_or_create(half=h, year=y)
#     terms_.append(t)

for i in range(1000, 1010):
    # User.objects.create_user(username=str(i), email=fake.email(), )
    first_name  = faker.first_name()
    last_name   = faker.last_name()
    name        = '{} {}'.format(first_name, last_name)
    email       = faker.email()
