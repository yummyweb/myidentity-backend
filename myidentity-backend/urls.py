"""mapsproblem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myiden import views

urlpatterns = [
    path(r'', views.home),
    path(r'create_person', views.create_person),
    #path(r'home', views.home),
    #path(r'tree1/', views.tree1),
    #path(r'accounts/profile/', views.profile),
    #path(r'postproblem/', views.postproblem),
    #path(r'postproblem2/', views.postproblem2),
    #path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')), 
]
