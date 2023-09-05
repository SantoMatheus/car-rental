from rest_framework import serializers
from car_rental.cars.serializers import CarRegisterOutputSerializer
from car_rental.users.serializers import CreateUserOutputSerializer
from car_rental.rents.models import Rent


class CreateRentInputSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=11, min_length=11)
    car = serializers.CharField(max_length=7, min_length=7)
    days_amount = serializers.CharField(max_length=1, min_length=2)


class CreateRentOutputSerializer(serializers.ModelSerializer):
    car = CarRegisterOutputSerializer()
    user = CreateUserOutputSerializer()

    model = Rent
    fields = ['days_amout', 'total_price', 'payment_status']
