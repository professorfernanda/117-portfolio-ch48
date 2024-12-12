from django.shortcuts import render
from .models import Project, Experience


# Create your views here.
def projects_list(request):

    projects = Project.objects.all()

    return render(
        request,
        "content/projects_list.html",
        {"projects" : projects }
    )


def experience_list(request):

    #get the info from the Admin panel
    experiences  = Experience.objects.all()

    return render(request, 
                "content/experience_list.html",  {'experiences' : experiences})
