from django.db import models

# Create your models here.

class LobReg2019(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=250)