# Generated by Django 2.1.7 on 2019-06-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_change_order_number_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('per_hour', 'per hour'), ('fixed', 'fixed')],
                                   default='per_hour', max_length=32, verbose_name='price type'),
        ),
    ]
