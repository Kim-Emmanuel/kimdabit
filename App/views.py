from datetime import datetime

from django.shortcuts import render, get_object_or_404
from .models import Profile, Photo, Project, Blog, SocialLink, Introduction, Job


# Create your views here
def home(request):
    intro = Introduction.objects.first()  # get the first introduction
    profile = Profile.objects.all()
    social_links = SocialLink.objects.all()
    jobs = Job.objects.all()  # get all jobs
    context = {'intro': intro, 'profile': profile, 'social_links': social_links, 'jobs': jobs}
    return render(request, 'home.html', context)


def about(request):
    profiles = Profile.objects.all()
    return render(request, 'about.html', {'profiles': profiles})


# Function for 'projects' page
def projects(request):
    project = Project.objects.all()
    context = {
        'projects': project
    }
    return render(request, 'projects.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


async def project(request, slug):
    project = await get_object_or_404(Project, slug=slug)
    fallbackImage = '/images/img.png'  # Define your fallback image URL here
    return render(request, 'projects.html', {'project': project, 'fallbackImage': fallbackImage})


# Function for 'photos' page
def photos(request):
    photo = Photo.objects.all()
    return render(request, 'photos.html', {'photos': photo})


# Function for 'blog' page
def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})


def current_year(request):
    context = {
        'current_year': datetime.now().year,
    }
    return render(request, 'footer.html', context)
