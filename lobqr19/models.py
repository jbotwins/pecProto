from django.db import models

# Create your models here.

class QuarterlyReport(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    phone = models.CharField(max_length=127)
    address = models.CharField(max_length=127)

class QR2019(models.Model):
    lobbyist_name = models.CharField(
        max_length=100,
        default="Joe Smoe"
    )