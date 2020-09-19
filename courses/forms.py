from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.forms import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control valid", 'placeholder': "First Name"}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control valid", 'placeholder': "Last Name"}))
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control valid", 'placeholder': "Username"}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': "form-control valid", 'placeholder': "Email"}))
    password1 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(
        attrs={'class': "form-control valid", 'placeholder': "Password"}))
    password2 = forms.CharField(label='Re-enter Password', max_length=100, widget=forms.PasswordInput(
        attrs={'class': "form-control valid", 'placeholder': "Re-enter Password"}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'group']


class CreateClassForm(ModelForm):
    name = forms.CharField(label='Class Name', max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control valid", 'placeholder': "Class Name"}))
    class_id = forms.CharField(label='Class Code', max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control valid", 'placeholder': "Class Code"}))

    class Meta:
        model = Class
        fields = ['name', 'class_id']


class CreateAssignmentForm(ModelForm):
    message = forms.CharField(label='Message', max_length=1000, widget=forms.Textarea(
        attrs={'class': "form-control valid"}))

    class Meta:
        model = Assignments
        fields = ['message', 'question']


class SubmitSolutionForm(ModelForm):
    class Meta:
        model = Solutions
        fields = ['answer']
