from django.urls import path

from car_rental.cars.views import CarRegisterViewSet

app_name = 'cars'

urlpatterns = [
    path('cars/register', CarRegisterViewSet.as_view(), name='car-register-viewset'),
]
