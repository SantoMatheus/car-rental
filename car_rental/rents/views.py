from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.authentication.auth_classes.app_authentication import AppAuthentication
from car_rental.rents.serializers import CreateRentInputSerializer, CreateRentOutputSerializer
from car_rental.rents.use_cases.create_rent_use_case import LegalRepresentativeRentCreateUseCase


class CreateRentViewSet(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=CreateRentInputSerializer(),
        responses={
            status.HTTP_201_CREATED: CreateRentOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rent_create_use_case = LegalRepresentativeRentCreateUseCase()

    def post(self, request: Request):
        serializer = CreateRentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['users']
        car_plate = serializer.validated_data['car_plate']
        days_amount = serializer.validated_data['days_amount']

        new_rent = self.rent_create_use_case.execute(user=user, days_amount=days_amount, car_plate=car_plate)
        output = CreateRentOutputSerializer(instance=new_rent)
        return Response(data=output.data, status=status.HTTP_201_CREATED)
