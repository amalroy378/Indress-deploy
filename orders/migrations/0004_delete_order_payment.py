# Generated by Django 4.1.7 on 2023-04-01 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_Payment',
        ),
    ]