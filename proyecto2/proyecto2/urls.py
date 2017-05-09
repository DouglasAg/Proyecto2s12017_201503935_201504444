"""proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from proyecto2 import views as pro_views

urlpatterns = [
    url(r'^$', pro_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'logdrive/', pro_views.logdrive),
    url(r'drivenew/', pro_views.drivenew),
    url(r'logingdrive/', pro_views.iniciar),
    url(r'nuevo/', pro_views.nuevoa, name='nuevo'),
    url(r'pridriv/', pro_views.pridive, name='pridrive'),
    url(r'moddrive/', pro_views.moddrive, name='moddrive'),
    url(r'nuevacarpeta/', pro_views.nuevacarpeta),
    url(r'cargararchivo/', pro_views.cargararchivo),
    url(r'historialdrive/', pro_views.historialdrive),
    url(r'historialcalendar/', pro_views.historialcalendar),
    url(r'nuevacarpeta/', pro_views.nuevacarpeta),
    url(r'cargararchivo/', pro_views.cargararchivo),
    url(r'logingcalendar/', pro_views.iniciarcalendar),
    url(r'calendarnew/', pro_views.calendarenew),
    url(r'listacalendar/', pro_views.listacalendar),
    url(r'listadrive/', pro_views.listadrive),
    

]
