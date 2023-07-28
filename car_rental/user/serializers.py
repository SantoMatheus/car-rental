from rest_framework import serializers

from car_rental.user.models import User


class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=11, min_length=11)
    cnpj = serializers.CharField(max_length=14, min_length=14)
    birth_date = serializers.DateTimeField()
    password = serializers.CharField(max_length=20)

class CreateUserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'cpf', 'birth_date']
