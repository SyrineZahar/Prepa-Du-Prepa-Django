from django.urls import path, re_path
from PrepaDuPrepa import views

urlpatterns = [
    path('users/', views.usersApi),
    re_path(r'^users/([0-9]+)$', views.usersApi),
    path('courses/', views.coursesApi),  
    re_path(r'^courses/([0-9]+)$', views.coursesApi),
]
