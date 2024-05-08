from .models import Payment
from django import forms
class Payment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        labels = {
            'order': '',
            'user': '',
            'restaurant': '',
            'amount': '',
            'timestamp': '',
            'status': '',
        }
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'restaurant': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'timestamp': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }      