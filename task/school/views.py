from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Class, Student
from django.http import Http404, HttpResponseRedirect


def main(request):
    all_classes = Class.objects.all()
    return render(request, 'school/main.html', {'classes': all_classes})


def grace(request):
    all_students = Student.objects.all()
    for student in all_students:
        if 30 <= student.score <= 35:
            student.score += 7
            student.save()
    return HttpResponseRedirect("/")

