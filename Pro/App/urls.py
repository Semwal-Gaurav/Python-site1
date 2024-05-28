"""
URL configuration for Pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.urls import path
from . import consumers

urlpatterns = [
    path('', views.home, name='home'),
    path('topic', views.topic, name='topic'),
    path('intro/', views.intro, name='intro'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('syntax/', views.syntax, name='syntax'),
    path('datatypes/', views.datatypes, name='datatypes'),
    path('numbers/', views.numbers, name='numbers'),
    path('functions/', views.functions, name='functions'),
    path('modules/', views.modules, name='modules'),
    path('loop/', views.loop, name='loop'),
    path('filehandling/', views.filehandling, name='filehandling'),
    path('chat/', views.chat_view, name='chat'),
    path('submit_message/', views.submit_message, name='submit_message'),
    path('change_path/<str:new_path>/', views.change_path, name='change_path'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

