from django.urls import path

from car_rental.cars.views import CarRegisterViewSet, CategorieRegisterViewSet

app_name = 'cars'

urlpatterns = [
    path('cars/register', CarRegisterViewSet.as_view(), name='car-register-viewset'),
    path('categories/register', CategorieRegisterViewSet.as_view(), name='categorie-register-viewset'),
]
