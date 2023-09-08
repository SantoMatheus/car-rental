from rest_framework import serializers

from car_rental.charges.serializers import ChargeOutputSerializer
from car_rental.payments.models import Payment


class PaymentInputSerializer(serializers.Serializer):
    charge = serializers.UUIDField()


class PaymentOutputSerializer(serializers.ModelSerializer):
    charge = ChargeOutputSerializer()

    class Meta:
        model = Payment
        fields = '__all__'
