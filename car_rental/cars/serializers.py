from rest_framework import serializers

from car_rental.cars.models import Car, CarCategorie


class CarRegisterInputSerializer(serializers.Serializer):

    chassis_number = serializers.CharField(max_length=17, min_length=17)
    manufacturer = serializers.CharField(max_length=50)
    categorie = serializers.ChoiceField(choices=CarCategorie.CarCategorieChoices.choices)
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
        fields = ['id', 'categorie', 'value']


class CarRegisterOutputSerializer(serializers.ModelSerializer):
    categorie = CategorieRegisterOutputSerializer()

    class Meta:
        model = Car
        fields = '__all__'


class CategorieEditInputSerializer(serializers.Serializer):
    categorie_name = serializers.CharField(max_length=30)
    value = serializers.FloatField()


class GetCarInputSerializer(serializers.Serializer):
    car_plate = serializers.CharField(min_length=7, max_length=7)


class GetCarOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
