"""
URL configuration for Appreciation_of_Wilderness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app01 import views
urlpatterns = [
    path('', views.index),
    path('init', views.index),
    path('register_u/', views.register_u),
    path('login_u/', views.login_u),
    path('login_a/', views.login_a),
    path('admin_init/', views.admin_init),
    path('logout/', views.logout_u,),
    path('user_init/', views.user_init),
    # path('find/', views.find),
    # app02的测试代码
    path("", include("app02.urls")),
]