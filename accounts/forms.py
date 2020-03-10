# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import User, Student
from django.contrib.admin.helpers import ActionForm
from university.models import Department

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_student', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

class StudentForm(forms.Form):
    display_name = forms.CharField(label='Display Name', max_length=128)
    phone_number = forms.CharField(label='Phone Number', max_length=128)
    telephone = forms.CharField(label='Telephone', max_length=128)
    address_1 = forms.CharField(label='Address', max_length=128)
    address_2 = forms.CharField(label='Address Cont\'d', max_length=128, required=False)

""" TODO: change this later when course is created """
class EnrollmentActionForm(ActionForm):
    course = forms.ChoiceField(
        label='Course:', 
        required=False, 
        choices=[(f.code, f.description) for f in Department.objects.all()]
    )