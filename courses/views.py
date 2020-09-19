from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from .models import *


def signupUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            groupName = str(form.cleaned_data.get('groups')[0])
            group = Group.objects.get(name=groupName)
            user.groups.add(group)
            if groupName == 'student':
                Student.objects.create(user=user)
            else:
                Teacher.objects.create(user=user)
            messages.success(request, 'user succesfully created')
            return redirect('loginUser')

    context = {'form': form}
    return render(request, 'signup.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in')
            groupName = request.user.groups.all()[0].name
            return redirect(f'{groupName}Dashboard')
        else:
            messages.info(request, "Invalid credentials")
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('loginUser')


def home(request):
    context = {}
    return render(request, 'home.html', context)


def teacherDashboard(request):
    context = {}
    return render(request, 'teacherDashboard.html', context)


def studentDashboard(request):
    context = {}
    return render(request, 'studentDashboard.html', context)
