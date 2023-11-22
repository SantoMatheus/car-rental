from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.authentication.auth_classes.app_authentication import AppAuthentication
from car_rental.payments.serializers import PaymentInputSerializer, PaymentOutputSerializer
from car_rental.payments.use_cases.payment_create_use_case import PaymentCreateUseCase


class PaymentViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payment_create_use_case = PaymentCreateUseCase()

    def post(self, request: Request):
        serializer = PaymentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        charge = serializer.validated_data['charge']

        payment = self.payment_create_use_case.execute(charge=charge)
        output = PaymentOutputSerializer(instance=payment)

        return Response(data=output.data, status=status.HTTP_201_CREATED)
