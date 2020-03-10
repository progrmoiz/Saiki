from django.db import models
from django.utils.translation import ugettext as _
import datetime

# Create your models here.
class University(models.Model):
    name = models.CharField(_('university name'), max_length=255)

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name

class Department(models.Model):
    code = models.CharField(_('code'), max_length=10, primary_key=True)
    description = models.CharField(_('description'), max_length=128)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Term(models.Model):
    HALF_CHOICES = (
        (1, 'Spring'),
        (2, 'Fall'),
    )
    half = models.IntegerField(_('half'), choices=HALF_CHOICES)
    year = models.IntegerField(_('year'), choices=year_choices(), default=current_year())

    class Meta:
        ordering = ['-year', '-half']


    def __str__(self):
        return '{} {}'.format(dict(self.HALF_CHOICES)[self.half], self.year)