from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu

class Order(models.Model):
    WAITING = 'waiting'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    STATUS_CHOICES = [
        (WAITING, 'Waiting'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu, through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=WAITING)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_address = models.TextField(blank=True, null=True)
    payment_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.menu_item.name}'

    def subtotal(self):
        return self.quantity * self.menu_item.price