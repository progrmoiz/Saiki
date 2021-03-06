# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.contrib.admin.helpers import ActionForm
from course.models import CourseOffering
from university.models import Term
from .models import User, Student

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_student', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

class StudentForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=128)
    last_name = forms.CharField(label='Last Name', max_length=128)
    display_name = forms.CharField(label='Display Name', max_length=128)
    email = forms.EmailField(label='Email', max_length=128)
    phone_number = forms.CharField(label='Phone Number', max_length=128)
    telephone = forms.CharField(label='Telephone', max_length=128, required=False)
    address_1 = forms.CharField(label='Address', max_length=128)
    address_2 = forms.CharField(label='Address Cont\'d', max_length=128, required=False)

class TeacherForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=128)
    last_name = forms.CharField(label='Last Name', max_length=128)
    display_name = forms.CharField(label='Display Name', max_length=128)
    email = forms.EmailField(label='Email', max_length=128)

class EnrollmentActionForm(ActionForm):
    try:
        try:
            term = Term.objects.all()[:1].get()
        except Term.DoesNotExist:
            term = None

        course = forms.ChoiceField(
            label='Course:',
            required=False,
            choices=[(f.id, f) for f in CourseOffering.objects.filter(term=term)]
        )
    except:
        pass