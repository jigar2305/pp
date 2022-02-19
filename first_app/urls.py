from django.contrib import admin
from django.urls import path,include
from first_app import views

urlpatterns = [
    path('userdata', views.userdata),
    path('add', views.add),
    path('UpdateData', views.UpdateData),
    path('CreateData', views.CreateData),
    path('DeleteData', views.DeleteData),
]