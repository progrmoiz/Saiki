from .models import AssignmentFile, AssignmentWorkFile
from django.forms import ModelForm
from django import forms

class AssignmentSubmissionForm(ModelForm):
    class Meta:
        model = AssignmentWorkFile
        fields = ['file', 'assignment_work']

class AssignmentMaterialForm(ModelForm):
    class Meta:
        model = AssignmentFile
        fields = ['file', 'assignment']

class AssignPointForm(forms.Form):
    points = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'col-2 form-control d-inline-block py-0'}), required=False, min_value=-1)

class AssignmentCreateForm(forms.Form):
    title = forms.CharField()
    points = forms.IntegerField()
    date = forms.DateField()
    time = forms.TimeField()
    description = forms.CharField(required=False)

class AssignmentEditForm(forms.Form):
    title = forms.CharField()
    points = forms.IntegerField()
    date = forms.DateField()
    time = forms.TimeField()
    description = forms.CharField(required=False)