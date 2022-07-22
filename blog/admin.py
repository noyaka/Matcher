from django.contrib import admin
from . import models

#tables admin can change
admin.site.register(models.Skill)
admin.site.register(models.Job)
admin.site.register(models.Candidate)