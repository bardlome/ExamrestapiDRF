"""exams_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
"""my
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
 
from exams_api import views
 
urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')), 
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Exams API', description='RESTAPI for Exams')),
 
    url(r'^$', views.api_root),
    url(r'^', include(('users.urls','users'), namespace='users')),
    url(r'^', include(('exams.urls','exams'), namespace='exams')),
    url(r'^', include(('examtasks.urls','examtasks'), namespace='examtasks')),
]





