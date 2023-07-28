from django.urls import path

from car_rental.rents.views import CreateRentViewSet

app_name = 'rents'

urlpatterns = [
    path('rents/create', CreateRentViewSet.as_view(), name='create-rent-viewset'),
]
