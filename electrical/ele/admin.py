from django.contrib import admin
from ele.models import CustomUser, Post, Lab, Research

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Lab)
admin.site.register(Research)