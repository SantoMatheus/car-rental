

from rest_framework import serializers

from car_rental.charges.models import Charge
from car_rental.rents.serializers import CreateRentOutputSerializer


class ChargeInputSerializer(serializers.Serializer):
    rent = serializers.UUIDField()


class ChargeOutputSerializer(serializers.ModelSerializer):
    rent = CreateRentOutputSerializer()

    class Meta:
        model = Charge
        fields = '__all__'
