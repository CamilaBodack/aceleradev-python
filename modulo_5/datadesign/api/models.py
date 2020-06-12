from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from django.core.validators import validate_ipv4_address
from django.core.exceptions import ValidationError


def level_validation(level):
    LEVEL_OPTIONS = ["CRITICAL", "DEBUG", "ERROR", "WARNING", "INFO"]
    if level not in LEVEL_OPTIONS:
        raise ValidationError("Level inválido")
    else:
        return level


class User(models.Model):
    name = models.CharField("Nome", max_length=50)
    last_login = models.DateTimeField("Último login", auto_now=True)
    email = models.EmailField("Email", max_length=254, validators=[EmailValidator])
    password = models.CharField(
        "Senha", max_length=50, validators=[MinLengthValidator(8)]
    )


class Agent(models.Model):
    name = models.CharField("Nome", max_length=50)
    status = models.BooleanField("Status",)
    env = models.CharField("Ambiente", max_length=20)
    version = models.CharField("Versão", max_length=5)
    address = models.TextField(
        "Endereço", max_length=39, validators=[validate_ipv4_address]
    )


class Event(models.Model):
    level = models.CharField("Level", max_length=20, validators=[level_validation])
    data = models.TextField("Data",)
    arquivado = models.BooleanField("Arquivado",)
    date = models.DateTimeField("Data", auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField("Nome", max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
