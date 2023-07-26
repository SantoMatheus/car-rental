"""
URL configuration for car_rental project.

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

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(title='Car Rental', default_version='0.1')
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-docs', schema_view.with_ui('swagger', cache_timeout=None)),
    path('api/v1/', include('car_rental.authentication.urls'), name='authentication'),
    path('api/v1/', include('car_rental.cars.urls'), name='cars'),
    path('api/v1/', include('car_rental.user.urls'), name='user'),
]
