"""
URL configuration for mySite project.

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
from django.contrib.auth import views as auth_views
from register import views as user_views
from personal import views

app_name = "Jelly Jumpers"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', include('personal.urls')),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name = "about"),
    path('Jelly_Jumpers/', views.Jelly_Jumpers, name = "Jelly_Jumpers"),
    path('contact/', views.contact, name = "contact"),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('blog/', views.Post, name='blog'),

]

