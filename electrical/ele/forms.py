from django import forms
from django.contrib.auth.forms import UserCreationForm
from ele.models import CustomUser, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'document']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email','name','bio','role' ,'company', 'subjects', 'profile_image')


class UserSearchForm(forms.Form):
    query = forms.CharField(max_length=100)