from rest_framework import serializers

from car_rental.users.models import LegalRepresentative, Company


class LegalRepresentativeRegisterInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=11, min_length=11)
    birth_date = serializers.DateTimeField()
    phone_number = serializers.CharField(max_length=11, min_length=11)
    zip_code = serializers.CharField(max_length=8, min_length=8)
    street_name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=12)


class LegalRepresentativeRegisterOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalRepresentative
        fields = ['name', 'cpf', 'birth_date', 'phone_number', 'zip_code', 'street_name', 'number', 'city', 'state',
                  'country']


class CompanyRegisterInputSerializer(serializers.Serializer):
    legal_representative = serializers.UUIDField()
    register_name = serializers.CharField(max_length=100)
    company_name = serializers.CharField(max_length=100)
    cnpj = serializers.CharField(max_length=14, min_length=14)
    phone_number = serializers.CharField(max_length=11, min_length=11)
    zip_code = serializers.CharField(max_length=8, min_length=8)
    street_name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=10, min_length=10)
    city = serializers.CharField(max_length=55)
    state = serializers.CharField(max_length=55)
    country = serializers.CharField(max_length=55)


class CompanyRegisterOutputSerializer(serializers.ModelSerializer):
    legal_representative = LegalRepresentativeRegisterOutputSerializer

    class Meta:
        model = Company
        fields = ['register_name', 'company_name', 'cnpj', 'phone_number', 'zip_code', 'street_name', 'number', 'city',
                  'state', 'country']


class SearchLegalRepresentativeInputSerializer(serializers.Serializer):
    cpf = serializers.CharField(max_length=11, min_length=11)
