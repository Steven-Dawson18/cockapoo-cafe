# Generated by Django 3.2.9 on 2022-01-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20220112_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(default=3.99),
        ),
    ]
