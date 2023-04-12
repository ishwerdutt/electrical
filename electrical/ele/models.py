from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.urls import reverse

from enum import Enum


class RoleChoices(Enum):
    ALUMNI = 'Alumni'
    FACULTY = 'Faculty'


class CustomUser(AbstractUser):
    role = models.CharField(choices=[(choice.value, choice.value) for choice in RoleChoices], max_length=10, null = True)
    bio = models.TextField(max_length=10000, null = True)
    name = models.TextField(max_length=30, null = True)
    company = models.TextField(null=True)
    subjects = models.CharField(max_length=50, null = True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        if self.role == RoleChoices.ALUMNI.value:
            return reverse('alumni_profile', args=[str(self.username)])
        elif self.role == RoleChoices.FACULTY.value:
            return reverse('faculty_profile', args=[str(self.username)])
        else:
            return reverse('')

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description= models.CharField(max_length=100,default="no short description available", blank=True)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return str(self.title) or ''

    def get_absolute_url(self):
        return reverse("post")
