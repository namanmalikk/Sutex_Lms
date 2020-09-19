from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def signupUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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
