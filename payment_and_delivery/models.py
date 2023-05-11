from django.db import models

# Create your models here.
from django.db import models
from order_management.models import Order
from django.contrib.auth.models import User

class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.address

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('NET_BANKING', 'Net Banking'),
        ('UPI', 'UPI'),
        ('CASH_ON_DELIVERY', 'Cash on Delivery'),
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.pk}"
