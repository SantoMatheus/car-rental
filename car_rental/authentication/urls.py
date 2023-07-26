from django.urls import path

from .views import AuthView

app_name = 'authentication'


urlpatterns = [
    path(app_name, AuthView.as_view(), name='auth-view'),
]
