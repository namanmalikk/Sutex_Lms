from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import CreateUserForm


def signupStudent(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request, 'user succesfully created')
            return redirect('home')

    context = {'form': form}
    return render(request, 'signup.html', context)


def loginStudent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in')
    context = {}
    return render(request, 'login.html', context)


def signupTeacher(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            messages.success(request, 'user succesfully created')
            return redirect('home')

    context = {'form': form}
    return render(request, 'signup.html', context)


def loginTeacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('home')


def home(request):
    context = {}
    return render(request, 'home.html', context)


def teacherDashboard(request):
    context = {}
    return render(request, 'teacherDashboard.html', context)


def studentDashboard(request):
    context = {}
    return render(request, 'studentDashboard.html', context)
