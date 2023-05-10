# Generated by Django 4.1.3 on 2023-05-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0005_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]