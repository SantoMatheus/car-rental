from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(title='Car Rental', default_version='0.1'),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-docs', schema_view.with_ui('swagger', cache_timeout=None)),
    path('api/v1/', include('car_rental.authentication.urls'), name='authentication'),
    path('api/v1/', include('car_rental.cars.urls'), name='cars'),
    path('api/v1/', include('car_rental.users.urls'), name='users'),
    path('api/v1/', include('car_rental.rents.urls'), name='rents'),
    path('api/v1/', include('car_rental.charges.urls'), name='charges'),
    path('api/v1/', include('car_rental.payments.urls'), name='payments'),
]
