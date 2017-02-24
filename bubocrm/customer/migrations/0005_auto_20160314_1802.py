# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-14 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20160314_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerType'),
        ),
        migrations.AlterField(
            model_name='customerattrval',
            name='cli_attr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerAttribute'),
        ),
        migrations.AlterField(
            model_name='customerattrval',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
        migrations.AlterField(
            model_name='customershablon',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Owner'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerType'),
        ),
    ]
