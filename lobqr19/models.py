from django.db import models

# Create your models here.

class QR2019(models.Model):
    dummy = models.CharField(
        max_length=127,
        default="default"
    )