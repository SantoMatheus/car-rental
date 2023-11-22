from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.rents.use_cases.get_rent_use_case import GetRentUseCase
from car_rental.rents.serializers import CreateRentInputSerializer, CreateRentOutputSerializer, GetRentOutputSerializer
from car_rental.rents.use_cases.create_rent_use_case import LegalRepresentativeRentCreateUseCase


class CreateRentViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rent_create_use_case = LegalRepresentativeRentCreateUseCase()

    def post(self, request: Request):
        serializer = CreateRentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        car_id = serializer.validated_data['car_id']
        days_amount = serializer.validated_data['days_amount']
        payment_method = serializer.validated_data['payment_method']

        new_rent = self.rent_create_use_case.execute(user=user, days_amount=days_amount, car=car_id,
                                                     payment_method=payment_method)
        output = CreateRentOutputSerializer(instance=new_rent)
        return Response(data=output.data, status=status.HTTP_201_CREATED)


class GetRentViewSet(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_rent_use_case = GetRentUseCase()

    def get(self, request: Request):
        rent = self.get_rent_use_case.execute()

        output = GetRentOutputSerializer(instance=rent, many=True)
        return Response(data=output.data, status=status.HTTP_200_OK)




