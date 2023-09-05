from django.urls import path

from car_rental.payments.views import PaymentViewSet

app_name = 'payments'

urlpatterns = [
    path('payments/create', PaymentViewSet.as_view(), name='payment-viewset')
    ]