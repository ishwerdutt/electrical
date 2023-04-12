from django.contrib import admin
from ele.models import CustomUser, Post, Lab

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Lab)