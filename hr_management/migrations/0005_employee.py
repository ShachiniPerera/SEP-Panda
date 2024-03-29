# Generated by Django 4.1.3 on 2023-05-10 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_management', '0004_profile_address_profile_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')),
                ('position', models.CharField(choices=[('manager', 'Manager'), ('waiter', 'Waiter'), ('chef', 'Chef'), ('cleaner', 'Cleaner')], default='waiter', max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
