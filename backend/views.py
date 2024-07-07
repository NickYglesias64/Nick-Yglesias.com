from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def home(request):

    return HttpResponse("Hello there")


def about(request):
    data = Project.objects.all()
    return render(request, 'about/about.html', {'project': data})


def detail(request, id):
    data = Project.objects.get(pk=id)
    return render(request, 'about/detail.html', {'project1': data})
