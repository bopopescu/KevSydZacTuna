from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


on_delete = models.DO_NOTHING
