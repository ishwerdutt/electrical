from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, CustomUser, RoleChoices
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'ele/index.html')

def acedemics(request):
    return render(request, 'ele/acedemics.html')


def under_gradutae_programmes(request):
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

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == RoleChoices.ALUMNI.value:
                return reverse('alumni_profile', kwargs={'username': user.username})
            if user.role == RoleChoices.FACULTY.value:
                return reverse('faculty_profile', kwargs={'username': user.username})
            if user.is_superuser:
                return reverse('index')
        return '/'

@login_required
def alumni_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, role = RoleChoices.ALUMNI.value)
    posts = Post.objects.filter(author=user)
    return render(request, 'ele/profile.html', {'user': user, 'posts': posts})

@login_required
def faculty_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, role = RoleChoices.FACULTY.value)
    posts = Post.objects.filter(author=user)
    return render(request, 'ele/profile.html', {'user': user, 'posts': posts})





def pflist(request):
    pfs = CustomUser.objects.filter(role = RoleChoices.FACULTY.value)
    context = {
        'pfs': pfs,

    }
    return render(request, 'ele/pf.html', context)


def allist(request):
    alumnies = CustomUser.objects.filter(role = RoleChoices.ALUMNI.value)
    context = {
        'alumnies': alumnies,

    }
    return render(request, 'ele/alumnies.html', context)



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.author.role == RoleChoices.ALUMNI.value:
                post.save()
                return redirect('alumni_profile', username = post.author)
            elif post.author.role == RoleChoices.FACULTY.value:
                post.save()
                return redirect('faculty_profile', username = post.author)
            elif post.author.is_superuser:
                post.save()
                return reverse('index')
            return redirect('index')
        else:
            pass
    else:
        form = PostForm()
    return render(request, 'ele/add_post.html', {'form': form})

