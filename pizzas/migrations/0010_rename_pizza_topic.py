# Generated by Django 4.2.2 on 2023-06-22 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0009_rename_topping_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizza',
            new_name='Topic',
        ),
    ]
