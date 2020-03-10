from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class PrevAcademicRecord(models.Model):
    college_name = models.CharField(_('college name'), max_length=128)
    year = models.IntegerField(_('year'), choices=year_choices(), default=current_year())
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    percentage = models.FloatField(_('percentage'))

class Guardian(models.Model):
    guardian_name = models.CharField(_('guardian name'), max_length=255)
    CNIC = models.CharField(_('CNIC'), max_length=13)
    phone_number = PhoneNumberField(_('phone number'))
    relationship = models.CharField(_('relationship'), max_length=255)
    occupation = models.CharField(_('occupation'), max_length=255)

class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    display_name = models.CharField(_('display name'), blank=True, max_length=128)
    dob = models.DateField(_('date of birth'), blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say')
    )
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(_('phone number'))
    telephone = PhoneNumberField(_('telephone'), blank=True)
    
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)

    CNIC = models.CharField(_('CNIC'), max_length=13)
    academic_records = models.OneToOneField(PrevAcademicRecord, on_delete=models.CASCADE)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username   

# @receiver(post_save, sender=User)
# def create_student_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_student_profile(sender, instance, **kwargs):
#     instance.profile.save()