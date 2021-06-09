from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title
