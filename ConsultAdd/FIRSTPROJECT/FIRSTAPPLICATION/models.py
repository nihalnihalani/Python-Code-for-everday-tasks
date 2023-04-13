from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=100)

class ID(models.Model):
    id = models.IntegerField()

class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
