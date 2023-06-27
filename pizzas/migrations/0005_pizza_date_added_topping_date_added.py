# Generated by Django 4.2.2 on 2023-06-22 04:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_remove_dough_pizza_delete_cheese_delete_dough'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topping',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
