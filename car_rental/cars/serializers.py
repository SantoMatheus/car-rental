from rest_framework import serializers

from car_rental.cars.models import Car


class CarRegisterInputSerializer(serializers.Serializer):

    chassis_number = serializers.CharField(max_length=17, min_length=17)
    manufacturer = serializers.CharField(max_length=50)
    categorie = serializers.CharField()
    manufacture_year = serializers.DateTimeField()
    model_year = serializers.DateTimeField()
    mileage = serializers.FloatField()
    color = serializers.CharField(max_length=50)
    fuel_type = serializers.CharField()
    fuel_level = serializers.CharField()

class CarRegisterOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['chassis_number', 'manufacturer', 'categorie', 'manufacture_year', 'model_year', 'mileage', 'color',
                  'fuel_type', 'fuel_level']
