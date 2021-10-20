from django.db import models
from datetime import datetime


# Create your models here.

class CameraBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drone(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    camera_brand_filter = models.ForeignKey(CameraBrand, on_delete=models.CASCADE, default=True, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    brand = models.CharField(max_length=200, null=False, blank=False)
    serial_number = models.CharField(max_length=200, null=False, blank=False)
    camera_model = models.CharField(max_length=200, null=False, blank=False)
    camera_megapixel = models.CharField(max_length=200, null=False, blank=False)
    camera_brand = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
