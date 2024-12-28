from django.contrib import admin
from django.urls import path

from telemedicineApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('myservice/', views.myservice, name='myservice'),
    path('appointment/', views.appointment, name='appointment'),
    path('deleteappointment/<int:id>', views.deleteappointment),
    path('show/', views.show, name='show'),
    path('deleteproduct/<int:id>', views.deleteproduct),
    path('contact/', views.contact, name='contact'),
    path('deletecontact/<int:id>', views.deletecontact),
    path('editappointment/<int:id>', views.editappointment, name='editappointment'),
    path('editproduct/<int:id>', views.editproduct, name='editproduct'),
    path('editcontact/<int:id>', views.editcontact, name='editcontact'),
    path('updateappointment/<int:id>', views.updateappointment, name='updateappointment'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('updatecontact/<int:id>', views.updatecontact, name='updatecontact'),
    path('product/', views.product, name='product'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),

]
