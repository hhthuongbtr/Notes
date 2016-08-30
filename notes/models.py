from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    def __str__(self):
        return self.subject_name


class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    pin = models.BooleanField(default=False)
    def __str__(self):
        return self.title

