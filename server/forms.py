from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Meal, MenuItem


class MenuForm(forms.Form):
    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
# class RestaurantForm(forms.ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = '__all__'
#         labels = {
#             'name': '',
#             'address': '',
#             'contact_number': '',
#             'operating_hours': '',
#             # Add label for surplus food availability here
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Restaurant Name'}),
#             'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
#             'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
#             'operating_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Operating Hours'}),
#             # Add widget for surplus food availability here
#         }

        

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        labels = {
            'name': '',
            'description': '',
            'price': '',
            # Add label for allergen information here
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meal Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            # 'availability': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # 'expiration_datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # # Add widget for allergen information here
        }

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         labels = {
#             'user': '',
#             'restaurant': '',
#             'meals': '',
#             'quantity': '',
#             'total_price': '',
#             'status': '',
#         }
#         widgets = {
#             'user': forms.Select(attrs={'class': 'form-control'}),
#             'restaurant': forms.Select(attrs={'class': 'form-control'}),
#             'meals': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#             'total_price': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

# class PaymentTransactionForm(forms.ModelForm):
#     class Meta:
#         model = PaymentTransaction
#         fields = '__all__'
#         labels = {
#             'order': '',
#             'user': '',
#             'restaurant': '',
#             'amount': '',
#             'timestamp': '',
#             'status': '',
#         }
#         widgets = {
#             'order': forms.Select(attrs={'class': 'form-control'}),
#             'user': forms.Select(attrs={'class': 'form-control'}),
#             'restaurant': forms.Select(attrs={'class': 'form-control'}),
#             'amount': forms.TextInput(attrs={'class': 'form-control'}),
#             'timestamp': forms.DateTimeInput(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

# class PickupLocationForm(forms.ModelForm):
#     class Meta:
#         model = PickupLocation
#         fields = '__all__'
#         labels = {
#             'name': '',
#             'address': '',
#             'operating_hours': '',
#             'contact_number': '',
#             'instructions': '',
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location Name'}),
#             'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
#             'operating_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Operating Hours'}),
#             'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
#             'instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instructions'}),
#         }


# class Restaurant(UserCreationForm):
#     class Meta:
#         model = Restaurant
#         fields = '__All__'


# class Meal(UserCreationForm):
#     class Meta:
#         model = Meal
#         fields = '__All__'


# class Order(UserCreationForm):
#     class Meta:
#         model = Order
#         fields = '__All__'

# class PaymentTransaction(UserCreationForm):
#     class Meta:
#         model = Order
#         fields = '__All__'

#         labels = {
#             'first_name':'',
#             'last_name':'',
#             'local_gov':'',
#             'phone_number': '',
#             'state':'',
#             'email':'',
#             'password':'',
#         }

#         widgets = {
#             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
#             'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
#             'state':forms.TextInput(attrs={'class':'form-control','placeholder':'state'}),
#             'local_gov':forms.TextInput(attrs={'class':'form-control','placeholder':'local goverment'}),
#             'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'mobile number'}),
#             'password':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
#             'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email address'}),
   
#         }

