from .excpetions.cpf_number_already_exists import CpfNumberAlreadyExists
from ..models import User


class CreateUserUseCase:
    def execute(self, name, cpf, birth_date, password):
        user_queryset = User.objects.filter(cpf=cpf)
        if user_queryset.exists() is True:
            raise CpfNumberAlreadyExists()

        user = User(name=name, cpf=cpf, birth_date=birth_date, username=cpf)
        user.set_password(raw_password=password)
        user.save()

        return user
