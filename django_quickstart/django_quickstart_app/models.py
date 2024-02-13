from django.db import models
from django.db.models import Index
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Country(models.Model):
    class Region(models.TextChoices):
        ASIA = "Asia"
        EUROPE = "Europe"
        AFRICA = "Africa"
        OCEANIA = "Oceania"
        AMERICAS = "Americas"

    alpha_code = models.CharField(max_length=3, primary_key=True)
    numeric_code = models.IntegerField()
    name = models.CharField(max_length=32)
    region = models.CharField(max_length=16, choices=Region, null=True)


class Address(models.Model):
    street_name = models.CharField(max_length=64)
    number = models.IntegerField()
    zip_code = models.IntegerField()
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)


class Person(models.Model):
    class Meta:
        indexes = [Index(fields=["first_name"]), Index(fields=["last_name"])]

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=256, null=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    birth_date = models.DateField(default=timezone.localdate)
    birth_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
