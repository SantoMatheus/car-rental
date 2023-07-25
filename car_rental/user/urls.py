from django.urls import path

from car_rental.user.views import CreateUserViewSet

app_name = 'user'

urlpatterns = [
    path('users/create', CreateUserViewSet.as_view(), name='create-user-viewset'),
]
