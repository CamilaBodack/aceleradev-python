from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.TextField(max_length=39)


class Event(models.Model):
    level = models.CharField(max_length=20)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateTimeField()
    agent_id = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Group(models.Model):
    name = models.CharField(max_length=50)


class GroupUser(models.Model):
    group_id = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
