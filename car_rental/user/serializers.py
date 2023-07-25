from rest_framework import serializers

from car_rental.user.models import User


class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=11)
    birth_date = serializers.DateTimeField()
    password = serializers.CharField(max_length=20)

class CreatUserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'cpf', 'birth_date']
