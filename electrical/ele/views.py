from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, CustomUser, RoleChoices
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

def index(request):
    return render(request, 'ele/index.html')


def labs(request):
    return render(request, 'ele/labs.html')

def academics(request):
    return render(request, 'ele/academics.html')


def under_graduate_programmes(request):
    return render(request, 'ele/undergraduate_programmes.html')



class AlumniPostListView(ListView):
    model = Post
    template_name = 'ele/post_list.html'

    def get_queryset(self):
        alumni_users = CustomUser.objects.filter(role=RoleChoices.ALUMNI.value)
        return Post.objects.filter(author__in=alumni_users)

class FacultyPostListView(ListView):
    model = Post
    template_name = 'ele/post_list.html'

    def get_queryset(self):
        faculty_users = CustomUser.objects.filter(role=RoleChoices.FACULTY.value)
        return Post.objects.filter(author__in=faculty_users)
    


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'ele/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'ele/loginpage.html'
    success_url = '/'

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == RoleChoices.ALUMNI.value:
                return reverse('user_profile', kwargs={'username': user.username})
            elif user.role == RoleChoices.FACULTY.value:
                return reverse('user_profile', kwargs={'username': user.username})
            elif user.is_superuser:
                return reverse('index')
            else:
                return super().get_success_url()
        else:
            return super().get_success_url()


@login_required(login_url="login")
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if user.role == RoleChoices.ALUMNI.value:
        posts = Post.objects.filter(author=user)
        return render(request, 'ele/profile.html', {'user': user, 'posts': posts})
    elif user.role == RoleChoices.FACULTY.value:
        posts = Post.objects.filter(author=user)

        return render(request, 'ele/profile.html', {'user': user, 'posts':posts})
    else:
        return HttpResponse('Invalid user role')
    


class UserListView(ListView):
    model = CustomUser
    template_name = 'ele/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        role = self.kwargs.get('role')
        if role == 'Faculty':
            queryset = CustomUser.objects.filter(role=RoleChoices.FACULTY.value)
        elif role == 'Alumni':
            queryset = CustomUser.objects.filter(role=RoleChoices.ALUMNI.value)
        else:
            queryset = CustomUser.objects.all()
        return queryset




@login_required(login_url="login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_profile', username = post.author)
    else:
        form = PostForm()
    return render(request, 'ele/add_post.html', {'form': form})

# logout view

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')