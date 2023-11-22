from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LegalRepresentativeRegisterInputSerializer, LegalRepresentativeRegisterOutputSerializer, \
    CompanyRegisterInputSerializer, CompanyRegisterOutputSerializer, SearchLegalRepresentativeOutputSerializer
from .use_cases.company_register__use_case import CompanyRegisterUseCase
from .use_cases.legal_representative_register_use_case import LegalRepresentativeRegisterUseCase
from .use_cases.search_company_use_case import SearchCompanyUseCase
from .use_cases.search_user_use_case import SearchLegalRepresentativeUseCase


class LegalRepresentativeRegisterViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legal_representative_register_use_case = LegalRepresentativeRegisterUseCase()

    def post(self, request: Request):
        serializer = LegalRepresentativeRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        cpf = serializer.validated_data['cpf']
        birth_date = serializer.validated_data['birth_date']
        phone_number = serializer.validated_data['phone_number']
        zip_code = serializer.validated_data['zip_code']
        street_name = serializer.validated_data['street_name']
        number = serializer.validated_data['number']
        city = serializer.validated_data['city']
        state = serializer.validated_data['state']
        country = serializer.validated_data['country']
        password = serializer.validated_data['password']

        legal_representative = self.legal_representative_register_use_case.execute(name=name, cpf=cpf,
                                                                                   birth_date=birth_date,
                                                                                   phone_number=phone_number,
                                                                                   zip_code=zip_code,
                                                                                   street_name=street_name,
                                                                                   number=number, city=city,
                                                                                   state=state, country=country,
                                                                                   password=password)
        output = LegalRepresentativeRegisterOutputSerializer(instance=legal_representative)
        return Response(data=output.data, status=status.HTTP_201_CREATED)


class SearchLegalRepresentativeViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_user_use_case = SearchLegalRepresentativeUseCase()

    def get(self, request: Request, cpf: str):
        legal_representative = self.search_user_use_case.execute(cpf=cpf)

        output = SearchLegalRepresentativeOutputSerializer(instance=legal_representative, many=True)

        return Response(data=output.data, status=status.HTTP_200_OK)


class CompanyRegisterViewSet(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_register_use_case = CompanyRegisterUseCase()

    def post(self, request: Request):
        serializer = CompanyRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        legal_representative = serializer.validated_data['legal_representative']
        register_name = serializer.validated_data['register_name']
        company_name = serializer.validated_data['company_name']
        cnpj = serializer.validated_data['cnpj']
        phone_number = serializer.validated_data['phone_number']
        zip_code = serializer.validated_data['zip_code']
        street_name = serializer.validated_data['street_name']
        number = serializer.validated_data['number']
        city = serializer.validated_data['city']
        state = serializer.validated_data['state']
        country = serializer.validated_data['country']

        new_company = self.company_register_use_case.execute(legal_representative=legal_representative,
                                                             register_name=register_name, company_name=company_name,
                                                             cnpj=cnpj, phone_number=phone_number, zip_code=zip_code,
                                                             street_name=street_name, number=number, city=city,
                                                             state=state, country=country)
        output = CompanyRegisterOutputSerializer(instance=new_company)
        return Response(data=output.data, status=status.HTTP_200_OK)


class SearchCompanyViewSet(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_company_use_case = SearchCompanyUseCase()

    def get(self, request: Request, cnpj: str):
        company = self.search_company_use_case.execute(cnpj=cnpj)

        output = CompanyRegisterOutputSerializer(instance=company)
        return Response(output.data, status=status.HTTP_200_OK)
