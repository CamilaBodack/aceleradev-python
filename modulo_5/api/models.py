from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from django.core.validators import validate_ipv4_address


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254, validators=[EmailValidator])
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.TextField(max_length=39, validators=[validate_ipv4_address])


class Event(models.Model):
    LEVELS_OPTIONS = (
        ("1", "CRITICAL"),
        ("2", "DEBUG"),
        ("3", "ERROR"),
        ("4", "WARNING"),
        ("5", "INFO"),
    )
    level = models.CharField(max_length=20, choices=LEVELS_OPTIONS)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Group(models.Model):
    name = models.CharField(max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
