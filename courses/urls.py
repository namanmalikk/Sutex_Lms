from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/dashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('student/dashboard/', views.studentDashboard, name='studentDashboard'),

    path('signup/', views.signupUser, name='signupUser'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
]
