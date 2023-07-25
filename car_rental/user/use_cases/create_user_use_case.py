from ..models import User


class CreateUserUseCase:
    def execute(self, name, cpf, birth_date, password):
        user = User(name=name, cpf=cpf, birth_date=birth_date, username=cpf)
        user.set_password(raw_password=password)
        user.save()

        return user
