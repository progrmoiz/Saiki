from django.db import models
from django.utils.translation import ugettext as _

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