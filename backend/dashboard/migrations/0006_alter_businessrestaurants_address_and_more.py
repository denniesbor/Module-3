# Generated by Django 4.0.3 on 2022-04-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_businessrestaurants_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessrestaurants',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='businessrestaurants',
            name='business_id',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='businessrestaurants',
            name='city',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='businessrestaurants',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='businessrestaurants',
            name='state',
            field=models.CharField(max_length=1000),
        ),
    ]
