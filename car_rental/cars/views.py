from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.authentication.auth_classes.app_authentication import AppAuthentication
from car_rental.cars.serializers import CarRegisterInputSerializer, CarRegisterOutputSerializer, \
    CategorieRegisterOutputSerializer, CategorieRegisterInputSerializer
from car_rental.cars.use_cases.car_register_use_case import CarRegisterUseCase
from car_rental.cars.use_cases.categorie_register_use_case import CategorieRegisterUseCase


class CategorieRegisterViewSet(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categorie_register_use_case = CategorieRegisterUseCase()

    @swagger_auto_schema(
        request_body = CategorieRegisterInputSerializer(),
        responses ={
            status.HTTP_201_CREATED: CategorieRegisterOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )

    def post(self, request: Request):
        serializer = CategorieRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        categorie = serializer.validated_data('categorie')
        value = serializer.validated_data('categorie')

        new_categorie = self.categorie_register_use_case.execute(categorie=categorie, value=value)

        output = CategorieRegisterOutputSerializer(instance=new_categorie)
        return Response(data=output.data, status=status.HTTP_201_CREATED)


class CarRegisterViewSet(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.car_register_use_case = CarRegisterUseCase()

    @swagger_auto_schema(
        request_body=CarRegisterInputSerializer(),
        responses={
            status.HTTP_201_CREATED: CarRegisterOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def post(self, request: Request):
        serializer = CarRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chassis_number = serializer.validated_data['chassis_number']
        manufacturer = serializer.validated_data['manufacturer']
        categorie = serializer.validated_data['categorie']
        manufacture_year = serializer.validated_data['manufacture_year']
        model_year = serializer.validated_data['model_year']
        mileage = serializer.validated_data['mileage']
        car_plate = serializer.validated_data['car_plate']
        color = serializer.validated_data['color']
        fuel_type = serializer.validated_data['fuel_type']
        fuel_level = serializer.validated_data['fuel_level']

        new_car = self.car_register_use_case.execute(chassis_number=chassis_number, manufacturer=manufacturer,
                                                     categorie=categorie, manufacture_year=manufacture_year,
                                                     model_year=model_year, mileage=mileage, car_plate=car_plate,
                                                     color=color, fuel_type=fuel_type, fuel_level=fuel_level)

        output = CarRegisterOutputSerializer(instance=new_car)
        return Response(data=output.data, status=status.HTTP_201_CREATED)

