# Generated by Django 4.0.3 on 2022-04-10 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_businessrestaurants_test_reviews_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BusinessRestaurants',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
