# client.models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.username 
    
class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey('server.Restaurant', on_delete=models.CASCADE, related_name='orders')
    meals = models.ManyToManyField('server.Meal')
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('ready', 'Ready for Pickup'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

class Payment(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('server.Restaurant', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
