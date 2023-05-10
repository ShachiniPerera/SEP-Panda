from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    
class Employee(models.Model):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    position_choices = [
        ('manager', 'Manager'),
        ('waiter', 'Waiter'),
        ('chef', 'Chef'),
        ('cleaner', 'Cleaner'),
    ]
    position = models.CharField(max_length=20, choices=position_choices)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name