from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateUserSerializer, CreateUserOutputSerializer
from .use_cases.create_user_use_case import CreateUserUseCase
from ..authentication.auth_classes.app_authentication import AppAuthentication


class CreateUserViewSet(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_user_use_case = CreateUserUseCase()

    @swagger_auto_schema(
        request_body=CreateUserSerializer(),
        responses={
            status.HTTP_201_CREATED: CreateUserOutputSerializer(),
            status.HTTP_400_BAD_REQUEST: 'Bad request.'
        }
    )
    def post(self, request: Request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        cpf = serializer.validated_data['cpf']
        birth_date = serializer.validated_data['birth_date']
        password = serializer.validated_data['password']

        user = self.create_user_use_case.execute(name=name, cpf=cpf, birth_date=birth_date, password=password)

        output = CreateUserOutputSerializer(instance=user)
        return Response(data=output.data, status=status.HTTP_201_CREATED)



