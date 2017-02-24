# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-15 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20160315_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldtype',
            options={'verbose_name': 'Тип поля', 'verbose_name_plural': '02 Типы полей'},
        ),
        migrations.AddField(
            model_name='customer',
            name='create_date',
            field=models.DateField(default=None, verbose_name='Дата заведения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerType', verbose_name='Тип клиента'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customershablon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerShablon', verbose_name='Шаблон клиента'),
        ),
        migrations.AlterField(
            model_name='customerattribute',
            name='attr_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.FieldType', verbose_name='Тип поля'),
        ),
        migrations.AlterField(
            model_name='customerattribute',
            name='customershablon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerShablon', verbose_name='Шаблон клиента'),
        ),
        migrations.AlterField(
            model_name='customerattrval',
            name='cli_attr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerAttribute', verbose_name='Атрибуты клиента'),
        ),
        migrations.AlterField(
            model_name='customerattrval',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='customershablon',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Owner', verbose_name='Контрагент'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerType', verbose_name='Тип клиента'),
        ),
    ]
