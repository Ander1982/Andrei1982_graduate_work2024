"""
URL configuration for car_service project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('works/', include('works.urls')),
    path('map/', views.map, name='map'),
    path('reg/', views.reguser, name='reguser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home'),
    path('work/', views.worker, name='worker'),
    path('login/', views.loginuser, name='loginuser'),
    path('telebot/', views.telegram, name='telebot'),
    path('thanks/', views.thanks_page, name='thanks'),
    path('record/', views.record, name='record'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
