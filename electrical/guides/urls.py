from django.urls import path
from . import views


urlpatterns = [
    path('guides/', views.guide, name =  "guides"),
    path('competitive_exams/', views.competitive_exam, name =  "exams"),

]