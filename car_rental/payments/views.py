from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.authentication.auth_classes.app_authentication import AppAuthentication
from car_rental.payments.serializers import PaymentInputSerializer, PaymentOutputSerializer
from car_rental.payments.use_cases.paymeny_create_use_case import Payment


class PaymentViewSet(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=PaymentInputSerializer(),
        responses={
            status.HTTP_201_CREATED: PaymentOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.payment_create_use_case = Payment()

    def post(self, request: Request):
        serializer = PaymentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        charge = serializer.validated_data['charge']
        value = serializer.validated_data['value']

        payment = self.payment_create_use_case.execute(charge_id=charge, value=value)
        output = PaymentOutputSerializer(instance=payment)

        return Response(data=output.data, status=status.HTTP_201_CREATED)
