from django.urls import path
from . import views
from .models import RoleChoices
from .views import signup,CustomLoginView, AlumniPostListView, FacultyPostListView, UserListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('acedemics/', views.acedemics, name='acedemics'),
    path('undergraduateprogrammes/', views.under_gradutae_programmes, name='undergraduateprogrammes'),
    path('alumni/posts/', AlumniPostListView.as_view(), name='alumni_posts'),
    path('faculty/posts/', FacultyPostListView.as_view(), name='faculty_posts'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('faculty/', UserListView.as_view(), {'role': 'Faculty'}, name='faculty_list'),
    path('alumni/', UserListView.as_view(), {'role': 'Alumni'}, name='alumni_list'),
    path('create_post/', views.create_post , name='create_post'),
]
