from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.authentication.auth_classes.app_authentication import AppAuthentication
from car_rental.charges.serializers import ChargeInputSerializer, ChargeOutputSerializer
from car_rental.charges.use_cases.create_charge_use_case import ChargeUseCase


class CreateChargeViewSet(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ChargeInputSerializer(),
        responses={
            status.HTTP_201_CREATED: ChargeOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payment_use_case = ChargeUseCase()

    def post(self, request: Request):
        serializer = ChargeInputSerializer(request=request.data)
        serializer.is_valid(raise_exception=True)

        rent = serializer.validated_data['rent']
        payment_method = serializer.validated_data['payment_method']

        new_charge = self.payment_use_case.execute(rent_id=rent, payment_method=payment_method)
        output = ChargeOutputSerializer(instance=new_charge)

        return Response(data=output.data, status=status.HTTP_201_CREATED)
