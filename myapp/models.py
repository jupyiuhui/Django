from io import StringIO
from time import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.timezone import now
# Create your models here.


class Employee(models.Model):
    Id = str(models.CharField(max_length=255))
    Social_Network = models.CharField(max_length=255)
    Key_word = models.CharField(max_length=255)
    Names = models.CharField(max_length=255)
    Link_post = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    comment = models.CharField( max_length=255)
    device = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    
class ThreadTask(models.Model):
    Minute = models.DateField(max_length=10)
    Hour = models.DateField(max_length=10)
    Day_of_month = models.DateField(max_length=10)
    Month = models.DateField(max_length=10)
    Day_of_week = models.DateField(max_length=10)

class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name