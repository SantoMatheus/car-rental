from rest_framework import serializers
from car_rental.cars.serializers import CarRegisterOutputSerializer
from car_rental.user.serializers import CreateUserOutputSerializer
from car_rental.rents.models import Rent


class CreateRentInputSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=11, min_length=11)
    car = serializers.CharField(max_length=7, min_length=7)
    start_date = serializers.CharField(max_length=10, min_length=10)
    end_date = serializers.CharField(max_length=10, min_length=10)

class CreateRentOutputSerializer(serializers.ModelSerializer):
    car = CarRegisterOutputSerializer()
    user = CreateUserOutputSerializer()

    model = Rent
    fields = ['start_date', 'end_date', 'total_price', 'payment_status']
