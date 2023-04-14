from django.urls import path
from . import views


urlpatterns = [
    path('guides/', views.guide, name =  "guides"),
    path('gsoc/', views.gsoc, name =  "gsoc"),
    path('noc/', views.noc, name =  "noc"),
    path('gate/', views.gate, name =  "gate"),

]