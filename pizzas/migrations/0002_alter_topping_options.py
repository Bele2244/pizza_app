# Generated by Django 4.2.2 on 2023-06-20 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'Toppings'},
        ),
    ]
