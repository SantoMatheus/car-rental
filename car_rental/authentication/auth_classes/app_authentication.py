from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission


class AppAuthentication(TokenAuthentication):
    model = Token


class MinhaPropria(BasePermission):
    message = 'Nao autenticado'

    def has_permission(self, request, view):
        if request.user.cpf == '1234':
            return True

        return False

