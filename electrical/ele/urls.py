from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import signup,CustomLoginView, alumni_profile, faculty_profile, AlumniPostListView, FacultyPostListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('acedemics/', views.acedemics, name='acedemics'),
    path('undergraduateprogrammes/', views.under_gradutae_programmes, name='undergraduateprogrammes'),
    path('alumni/posts/', AlumniPostListView.as_view(), name='alumni_posts'),
    path('faculty/posts/', FacultyPostListView.as_view(), name='faculty_posts'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('alumni/<str:username>/', alumni_profile, name='alumni_profile'),
    path('faculty/<str:username>/', faculty_profile, name='faculty_profile'),
    path('pfs/', views.pflist, name='pflist'),
    path('alumnies/', views.allist, name='allist'),
    path('create_post/', views.create_post , name='create_post'),
]
