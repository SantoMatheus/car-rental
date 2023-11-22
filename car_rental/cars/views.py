from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car_rental.cars.serializers import CarRegisterInputSerializer, CarRegisterOutputSerializer, \
    CategorieRegisterOutputSerializer, CategorieRegisterInputSerializer, CategorieEditInputSerializer, \
    GetCarOutputSerializer
from car_rental.cars.use_cases.car_register_use_case import CarRegisterUseCase
from car_rental.cars.use_cases.categorie_edit_use_case import CategorieEditUseCase
from car_rental.cars.use_cases.categorie_register_use_case import CategorieRegisterUseCase
from car_rental.cars.use_cases.get_car_use_case import GetCarUseCase
from car_rental.cars.use_cases.get_categorie_use_case import GetCategorieUseCase


class CategorieRegisterViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categorie_register_use_case = CategorieRegisterUseCase()

    def post(self, request: Request):
        serializer = CategorieRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        categorie = serializer.validated_data['categorie']
        value = serializer.validated_data['value']

        new_categorie = self.categorie_register_use_case.execute(categorie=categorie, value=value)

        output = CategorieRegisterOutputSerializer(instance=new_categorie)
        return Response(data=output.data, status=status.HTTP_201_CREATED)


class CarRegisterViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.car_register_use_case = CarRegisterUseCase()

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


class CategorieEditViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categorie_edit_use_case = CategorieEditUseCase()

    def patch(self, request: Request, id_categorie: str):
        serializer = CategorieEditInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        categorie_name = serializer.validated_data['categorie_name']
        value = serializer.validated_data['value']

        categorie = self.categorie_edit_use_case.execute(id_categorie=id_categorie,
                                                         categorie_name=categorie_name, new_value=value)
        output = CategorieRegisterOutputSerializer(instance=categorie)

        return Response(data=output.data, status=status.HTTP_200_OK)


class GetCategorieViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_categorie_use_case = GetCategorieUseCase()

    def get(self, request: Request):
        car_categorie = self.get_categorie_use_case.execute()
        output = CategorieRegisterOutputSerializer(instance=car_categorie, many=True)

        return Response(data=output.data, status=status.HTTP_200_OK)


class GetCarViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_car_use_case = GetCarUseCase()

    def get(self, request: Request, car_plate: str):
        car = self.get_car_use_case.execute(car_plate=car_plate)

        output = CarRegisterOutputSerializer(instance=car, many=True)
        return Response(data=output.data, status=status.HTTP_200_OK)
