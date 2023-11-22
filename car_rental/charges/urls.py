from django.urls import path

from car_rental.charges.views import CreateChargeViewSet


app_name = 'charges'

urlpatterns = [
    path('charge/create', CreateChargeViewSet.as_view(), name='create-charge-viewset')
    ]