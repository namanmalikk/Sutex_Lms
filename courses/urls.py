from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher/dashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('student/dashboard/', views.studentDashboard, name='studentDashboard'),

    path('teacher/newclass/', views.createClass, name='createClass'),
    path('student/newclass/', views.joinClass, name='joinClass'),

    path('teacher/class/<str:pk>/',
         views.teacherClassView, name='teacherClassView'),
    path('teacher/class/<str:pk>/students/',
         views.enrolledStudents, name='enrolledStudents'),
    path('student/class/<str:pk>/',
         views.studentClassView, name='studentClassView'),
    path('student/class/<str:pk>/<str:pk2>',
         views.detailAssignment, name='detailAssignment'),
    path('teacher/class/<str:pk>/<str:pk2>',
         views.submittedAnswers, name='submittedAnswers'),

    path('signup/', views.signupUser, name='signupUser'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
]
