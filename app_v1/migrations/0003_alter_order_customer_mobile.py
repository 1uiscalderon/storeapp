# Generated by Django 3.2 on 2021-04-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0002_alter_order_customer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_mobile',
            field=models.CharField(max_length=40),
        ),
    ]
