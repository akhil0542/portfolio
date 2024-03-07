from django.shortcuts import render, HttpResponseRedirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', context={'projects': projects, 'project': 'active'})

def project_detail(request, pk):
    project = Project.objects.get(pk = pk)
    return render(request, 'projects/project_detail.html', context={'project': project})

def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                technology = form.cleaned_data['technology']
                image = form.cleaned_data['image']
                project = Project(title=title, description=description, technology=technology, image=image)
                project.save()
                return HttpResponseRedirect('/projects/')
        else:
            form = ProjectForm()
        return render(request, 'projects/addproject.html', context={'form': form, 'add_project': 'active'})
    else:
        return HttpResponseRedirect('/login/')
    
def update_project(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            project = Project.objects.get(pk=id)
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(f'/projects/{id}/')
        else:
            project = Project.objects.get(pk=id)
            form = ProjectForm(instance=project)
        return render(request, 'projects/updateproject.html', context={'form': form, 'id': id})
    else:
        return HttpResponseRedirect('/login/')    
    
def delete_project(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            project = Project.objects.get(pk=id)
            project.delete()
        return HttpResponseRedirect('/projects/')
    else:
        return HttpResponseRedirect('/login/')    