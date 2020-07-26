from django.db import models
import uuid


# Create your models here.

class user(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=255)
