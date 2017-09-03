from django.db import models
from django.core.urlresolvers import reverse


class Class(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    sec = models.ForeignKey(Class, on_delete=models.CASCADE)
    stud_name = models.CharField(max_length=100)
    score = models.IntegerField(default=100)

    def __str__(self):
        return self.stud_name

