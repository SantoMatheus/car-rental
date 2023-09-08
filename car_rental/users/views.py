from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LegalRepresentativeRegisterInputSerializer, LegalRepresentativeRegisterOutputSerializer, \
    SearchLegalRepresentativeInputSerializer, CompanyRegisterInputSerializer, CompanyRegisterOutputSerializer
from .use_cases.company_register__use_case import CompanyRegisterUseCase
from .use_cases.legal_representative_register_use_case import LegalRepresentativeRegisterUseCase
from .use_cases.search_user_use_case import SearchLegalRepresentativeUseCase
from ..authentication.auth_classes.app_authentication import AppAuthentication


class LegalRepresentativeRegisterViewSet(APIView):
    permission_classes = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legal_representative_register_use_case = LegalRepresentativeRegisterUseCase()

    @swagger_auto_schema(
        request_body=LegalRepresentativeRegisterInputSerializer(),
        responses={
            status.HTTP_201_CREATED: LegalRepresentativeRegisterOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
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
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=SearchLegalRepresentativeInputSerializer(),
        responses={
            status.HTTP_201_CREATED: LegalRepresentativeRegisterOutputSerializer,
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.search_user_use_case = SearchLegalRepresentativeUseCase()

    def get(self, request: Request, cpf: str):
        serializer = SearchLegalRepresentativeInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        legal_representative = self.search_user_use_case.execute(cpf=cpf)
        output = LegalRepresentativeRegisterOutputSerializer(instance=legal_representative)

        return Response(data=output.data, status=status.HTTP_200_OK)


class CompanyRegisterViewSet(APIView):
    permission_classes = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_register_use_case = CompanyRegisterUseCase()

    @swagger_auto_schema(
        request_body=CompanyRegisterInputSerializer(),
        responses={
            status.HTTP_201_CREATED: CompanyRegisterOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def post(self, request: Request):
        serializer = LegalRepresentativeRegisterInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        legal_representative = serializer.validated_data['legal_representative']
        register_name = serializer.validated_data['register_name']
        company_name = serializer.validated_data['company_name']
        cnpj = serializer.validated_data['cnpj']
        phone_number = serializer.validated_data['phone_number']
        cep = serializer.validated_data['cep']
        street_name = serializer.validated_data['street_name']
        number = serializer.validated_data['number']
        city = serializer.validated_data['city']
        state = serializer.validated_data['state']
        country = serializer.validated_data['country']

        new_company = self.company_register_use_case.execute(legal_representative=legal_representative,
                                                             register_name=register_name, company_name=company_name,
                                                             cnpj=cnpj, phone_number=phone_number, zip_code=cep,
                                                             street_name=street_name, number=number, city=city,
                                                             state=state, country=country)
        output = LegalRepresentativeRegisterOutputSerializer(instance=new_company)
        return Response(data=output.data, status=status.HTTP_201_CREATED)
