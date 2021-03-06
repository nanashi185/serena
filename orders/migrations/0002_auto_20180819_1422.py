# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='claim',
            field=models.CharField(choices=[('delivery', 'Delivery'), ('pickup', 'Pickup')], default='delivery', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('paypal', 'PayPal')], default='paypal', max_length=10),
        ),
    ]
