from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.Userlogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.ulogout, name='logout'),
    path('charge/', views.charge, name="charge"),
    path('list/<int:id>', views.list, name='list'),
    path('proceedcheckout/', views.proceedcheckout, name='proceedcheckout'),
]