# Generated by Django 3.2.9 on 2022-02-01 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menuitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='slug',
        ),
    ]
