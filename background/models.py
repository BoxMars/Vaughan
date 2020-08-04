from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class user(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=255)
    group=models.CharField(max_length=200,default='User')
    created = models.DateTimeField(default=timezone.now)

class article(models.Model):
    author=models.ForeignKey(user,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    body=models.TextField()
