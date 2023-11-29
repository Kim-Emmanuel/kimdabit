from django.db import models


# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField(null=True, blank=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    url = models.URLField()

    def __str__(self):
        return self.name


class Introduction(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(default='Default description')


class Profile(models.Model):
    fullName = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    fullBio = models.TextField()
    profileImage = models.ImageField(upload_to='images/')
    resumeURL = models.URLField()
    email = models.EmailField()
    social_links = models.ManyToManyField(SocialLink)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.fullName


class Technology(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(default='Default description')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(default='Default description')
    logo = models.ImageField(upload_to='logos/', null=True)

    name = models.CharField(max_length=200, null=True)
    tagline = models.CharField(max_length=500, null=True)
    projectUrl = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='fallback_images/', null=True)
    technologies = models.ManyToManyField(Technology)
    overview = models.TextField(null=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    # Define your fields for Photo model here
    pass


class Blog(models.Model):
    # Define your fields for Blog model here
    pass
