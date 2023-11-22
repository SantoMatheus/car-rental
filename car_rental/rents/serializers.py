from rest_framework import serializers
from car_rental.cars.serializers import CarRegisterOutputSerializer
from car_rental.users.serializers import LegalRepresentativeRegisterOutputSerializer, CompanyRegisterOutputSerializer
from car_rental.rents.models import Rent


class CreateRentInputSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=11, min_length=11)
    car_id = serializers.UUIDField()
    days_amount = serializers.IntegerField()
    payment_method = serializers.ChoiceField(choices=Rent.PaymentMethodChoices.choices)


class CreateRentOutputSerializer(serializers.ModelSerializer):
    car = CarRegisterOutputSerializer()
    user = LegalRepresentativeRegisterOutputSerializer()

    class Meta:
        model = Rent
        fields = ['id', 'user', 'car', 'days_amount', 'total_price', 'payment_method', 'payment_status']


class GetRentOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
