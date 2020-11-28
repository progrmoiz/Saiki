from django import forms

class GradeForm(forms.Form):

    GRADE_POINT_EQUIVALENT = (
        (None, 'Select Grade'),
        (4.00, 'A'),
        (3.67, 'A-'),
        (3.33, 'B+'),
        (3.00, 'B'),
        (2.67, 'B-'),
        (2.33, 'C+'),
        (2.00, 'C'),
        (1.67, 'D'),
        (0.00, 'F'),
    )

    grade = forms.FloatField(widget=forms.Select(choices=GRADE_POINT_EQUIVALENT, attrs={'class': 'form-control'}), required=False)