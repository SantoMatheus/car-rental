from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from car_rental.authentication.serializers import CustomAuthTokenSerializer, AuthOutputSerializer


class AuthView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    @swagger_auto_schema(
        responses={400: 'Bad request', 200: AuthOutputSerializer},
        request_body=CustomAuthTokenSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)
