from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    name = models.CharField("Nome", max_length=50)
    last_login = models.DateTimeField("Último login", auto_now=True)
    email = models.EmailField("Email")
    password = models.CharField(
        "Senha", max_length=50, validators=[MinLengthValidator]
    )


class Agent(models.Model):
    name = models.CharField("Nome", max_length=50)
    status = models.BooleanField("Status", default=True)
    env = models.CharField("Ambiente", max_length=20)
    version = models.CharField("Versão", max_length=5)
    address = models.GenericIPAddressField("Endereço", protocol="IPv4")


class Event(models.Model):
    LEVEL_CHOICES = (
        ("1", "CRITICAL"),
        ("2", "DEBUG"),
        ("3", "ERROR"),
        ("4", "WARNING"),
        ("5", "INFO"),
    )
    level = models.CharField("Level", max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField("Data")
    arquivado = models.BooleanField("Arquivado", default=False)
    date = models.DateTimeField("Data", auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField("Nome", max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
