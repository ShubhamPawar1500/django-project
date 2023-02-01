"""zomato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('home/users/', views.user_page, name='user'),
    path('home/upload_u', views.upload_user, name='upload_user'),
    path('home/users/update_u/<str:name>', views.edit_user, name='edit_user'),
    path('home/users/del_u/<str:name>', views.del_user),
    path('home/food/', views.food_page, name='foodpage'),
    path('home/upload_f', views.upload_food, name='upload_food'),
    path('home/upload_r', views.upload_review, name='upload_review'),
    path('home/food/update/<int:id>', views.edit_food),
    path('home/food/delete/<int:id>', views.del_food),
    path('home/edit/<int:id>', views.edit_rating),
    path('home/delete/<int:id>', views.del_rating),
    path('register/', views.register, name='registerpage'),
    path('logout/', views.logout_request, name='logout'),
    path('',views.login_request, name='login')
]
