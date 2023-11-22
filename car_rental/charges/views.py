
from rest_framework import status

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from car_rental.charges.serializers import ChargeInputSerializer, ChargeOutputSerializer
from car_rental.charges.use_cases.create_charge_use_case import ChargeUseCase


class CreateChargeViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payment_use_case = ChargeUseCase()

    def post(self, request: Request):
        serializer = ChargeInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        rent = serializer.validated_data['rent']

        new_charge = self.payment_use_case.execute(rent_id=rent)
        output = ChargeOutputSerializer(instance=new_charge)

        return Response(data=output.data, status=status.HTTP_201_CREATED)
