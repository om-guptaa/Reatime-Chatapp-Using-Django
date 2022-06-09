from datetime import datetime
import imp
from pyexpat import model
from django.db import models
from django.forms import CharField
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)
