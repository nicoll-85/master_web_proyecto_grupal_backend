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

from administrator.urls import router as admin_router
from authentication.urls import router as auth_router
from gym.urls import router as gym_router

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/admin/', include(admin_router.urls)),
    path('api/auth/', include(auth_router.urls)),
    path('api/gym/', include(gym_router.urls)),
    path('api/', include('gym.urls')),
    ]
