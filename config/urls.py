"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #Admin urls
    path('admin/', admin.site.urls),

    #Token urls
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    #Auth needed urls
    path('Businesses/', include('apps.Businesses.urls')),
    path('CircuitBreakers/', include('apps.CircuitBreakers.urls')),
    path('Connectors/', include('apps.Connectors.urls')),
    path('Javelins/', include('apps.Javelins.urls')),
    path('Measurements/', include('apps.Measurements.urls')),
    path('Outlets/', include('apps.Outlets.urls')),
    path('Panels/', include('apps.Panels.urls')),
    path('Sectors/', include('apps.Sectors.urls')),
    path('Tools/', include('apps.Tools.urls')),
    path('Images/', include('apps.Images.urls')),
]
