from django.urls import path

from car_rental.users.views import LegalRepresentativeRegisterViewSet

app_name = 'users'

urlpatterns = [
    path('users/create', LegalRepresentativeRegisterViewSet.as_view(), name='create-users-viewset'),
]
