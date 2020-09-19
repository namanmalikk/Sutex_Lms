from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/dashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('student/dashboard/', views.studentDashboard, name='studentDashboard'),

    path('teacher/signup/', views.signupTeacher, name='signupTeacher'),
    path('teacher/login/', views.loginTeacher, name='loginTeacher'),
    path('student/signup/', views.signupStudent, name='signupStudent'),
    path('student/login/', views.loginStudent, name='loginStudent'),

    path('logout/', views.logoutUser, name='logoutUser'),
]
