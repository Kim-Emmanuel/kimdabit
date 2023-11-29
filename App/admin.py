from django.contrib import admin
from .models import Profile, SocialLink, Introduction, Job, Project, Technology, Skill

# Register your models here.


admin.site.register(Skill)
admin.site.register(Technology)
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Introduction)
admin.site.register(Profile)
admin.site.register(SocialLink)
