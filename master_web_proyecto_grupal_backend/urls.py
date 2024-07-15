"""
URL configuration for master_web_proyecto_grupal_backend project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from administrator.urls import router as router_admin
from authentication.urls import router as router_auth
from gym.urls import router as router_gym

urlpatterns = [
    path("admin/", admin.site.urls),
    #path(f"{settings.BASE_URL}auth/", include(router_auth)),
    #path(f"{settings.BASE_URL}admin/", include(router_admin)),
    #path(f"{settings.BASE_URL}gym/", include(router_gym)),
    path('api/', include('gym.urls')),
    ]
