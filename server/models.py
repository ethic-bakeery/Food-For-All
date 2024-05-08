# server.models
from django.db import models


from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)  # Note: This should be a CharField, not a reference to name
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)  # Allow null and blank values
    operating_hours = models.CharField(max_length=100, null=True, blank=True)  # Allow null and blank values
    created_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField('client.User', related_name='followed_restaurants', blank=True)
    
class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.IntegerField()

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
