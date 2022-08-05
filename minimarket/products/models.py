from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
