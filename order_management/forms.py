from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class OrderStatusForm(forms.ModelForm):
    STATUS_CHOICES = Order.STATUS_CHOICES
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Order
        fields = ['status']
