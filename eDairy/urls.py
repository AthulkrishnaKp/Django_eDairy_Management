"""eDairy URL Configuration

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
from dairy.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration', registration, name='registration'),
    path('user_login', user_login, name='user_login'),
    path('user_home', user_home, name='user_home'),
    path('manageCategory', manageCategory, name='manageCategory'),
    path('editCategory/<int:pid>', editCategory, name='editCategory'),
    path('deleteCategory/<int:pid>', deleteCategory, name='deleteCategory'),
    path('manageNotes', manageNotes, name='manageNotes'),
    path('editNotes/<int:pid>', editNotes, name='editNotes'),
    path('viewNotes/<int:pid>', viewNotes, name='viewNotes'),
    path('deleteNotesHistory/<int:pid>', deleteNotesHistory, name='deleteNotesHistory'),
    path('deleteNotes/<int:pid>', deleteNotes, name='deleteNotes'),
    path('searchNotes', searchNotes, name='searchNotes'),
    path('profile', profile, name='profile'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
