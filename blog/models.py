from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

# table Skill
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#table Job
class Job(models.Model):
    title = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skill, blank=True)
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse("blog:candidate", args=[self.pk])
        
    def __str__(self):
        return self.title

#table Candidate
class Candidate(models.Model):
    title = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skill, blank=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title