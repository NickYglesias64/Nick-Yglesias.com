from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Project


def home(request):

    return HttpResponse("Hello there")


def projects(request):
    data = Project.objects.all()
    return render(request, 'projects/projects.html', {'project': data})


def detail(request, id):
    data = Project.objects.get(pk=id)
    return render(request, 'projects/detail.html', {'detail': data})


def add(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    if title and description:
        project = Project(title=title, description=description)
        project.save()
        return HttpResponseRedirect('/projects')

    return render(request, 'projects/add.html')


def delete(request, id):
    try:
        project = Project.objects.get(pk=id)
    except:
        raise Http404('Project does not exist')
    project.delete()
    return HttpResponseRedirect('/projects')
