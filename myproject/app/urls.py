from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login_action',views.login_action,name='login_action'),
    path('logout',auth_views.LogoutView.as_view(),name="logout"),
    path('classes',views.classes,name='classes'),
    path('create_class',views.create_class,name='create_class'),
    path('subject_url',views.subject,name='subject_url'),
    path('create_subject',views.create_subject,name='create_subject'),
    path('assign_subject',views.assign_subject,name='assign_subject'),
    path('create_assign_subject',views.create_assign_subject,name='create_assign_subject'),
    path('student',views.student,name='student'),
    path('create_student',views.create_student,name='create_student'),
    path('assign_student',views.assign_student,name='assign_student'),
    path('create_assign_student',views.create_assign_student,name='create_assign_student'),
    path('exam',views.exam,name='exam'),
    path('create_exam',views.create_exam,name='create_exam'),
    path('exam_subject',views.exam_subject,name='exam_subject'),
    path('create_exam_subject',views.create_exam_subject,name='create_exam_subject'),
    path('question',views.question,name='question'),
    path('create_question',views.create_question,name='create_question'),
    path('user',views.user,name='user'),
    path('create_user',views.create_user,name='create_user'),
    path('student_login',views.student_login,name='student_login'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('multiple_exam',views.multiple_exam,name='multiple_exam'),
    path('exam_form',views.exam_form,name='exam_form'),

    path('demo',views.demo,name='demo'),
    path('demo_action',views.demo_action,name='demo_action'),
    

    

    






]