from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import CreateUserForm, CreateClassForm, CreateAssignmentForm
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
    teacher = request.user.teacher
    classes = teacher.class_set.all()
    context = {'classes': classes}
    return render(request, 'teacherDashboard.html', context)


def studentDashboard(request):
    student = request.user.student
    classes = Class.objects.filter(students=student)
    context = {'classes': classes}
    return render(request, 'studentDashboard.html', context)


def createClass(request):
    form = CreateClassForm()
    if request.method == 'POST':
        form = CreateClassForm(request.POST)
        if form.is_valid():
            new_class = form.save()
            new_class.teacher = request.user.teacher
            new_class.save()
            return redirect('teacherDashboard')
    context = {'form': form}
    return render(request, 'createClass.html', context)


def joinClass(request):
    if request.method == 'POST':
        id = request.POST.get('class_id')
        try:
            myClass = Class.objects.get(class_id=id)
            student = request.user.student
            myClass.students.add(student)
            return redirect('studentDashboard')
        except Class.DoesNotExist:
            messages.info(request, "Invalid id")
    context = {}
    return render(request, 'joinClass.html', context)


def teacherClassView(request, pk):
    # teacher = request.user.teacher
    class_object = Class.objects.get(class_id=pk)
    form = CreateAssignmentForm()
    if request.method == 'POST':
        form = CreateAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            assignment.class_object = class_object
            assignment.save()
            return redirect('teacherDashboard')
    assignments = class_object.assignments_set.all()
    context = {'assignments': assignments, 'class': class_object, 'form': form}
    return render(request, 'teacherClassView.html', context)


def studentClassView(request, pk):
    # student = request.user.student
    class_object = Class.objects.get(class_id=pk)
    assignments = class_object.assignments_set.all()
    context = {'assignments': assignments, 'class': class_object}
    return render(request, 'studentClassView.html', context)
