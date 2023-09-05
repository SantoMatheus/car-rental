from rest_framework import serializers

from car_rental.cars.models import Car, CarCategorie


class CarRegisterInputSerializer(serializers.Serializer):

    chassis_number = serializers.CharField(max_length=17, min_length=17)
    manufacturer = serializers.CharField(max_length=50)
    categorie = serializers.CharField()
    manufacture_year = serializers.DateTimeField()
    model_year = serializers.DateTimeField()
    mileage = serializers.FloatField()
    car_plate = serializers.CharField(min_length=7, max_length=7)
    color = serializers.CharField(max_length=50)
    fuel_type = serializers.CharField()
    fuel_level = serializers.CharField()


class CategorieRegisterInputSerializer(serializers.Serializer):
    categorie = serializers.CharField(max_length=30)
    value = serializers.FloatField()

class CategorieRegisterOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategorie
        fields = ['categorie', 'value']

class CarRegisterOutputSerializer(serializers.ModelSerializer):
    type = CategorieRegisterOutputSerializer()

    class Meta:
        model = Car
        fields = '__all__'
