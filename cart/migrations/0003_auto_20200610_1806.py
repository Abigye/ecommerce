# Generated by Django 3.0.7 on 2020-06-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
