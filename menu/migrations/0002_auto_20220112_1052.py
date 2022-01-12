# Generated by Django 3.2.9 on 2022-01-12 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cake',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='colddrinks',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='hotdrinks',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.RemoveField(
            model_name='sandwich',
            name='likes',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='menuitems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Cake',
        ),
        migrations.DeleteModel(
            name='ColdDrinks',
        ),
        migrations.DeleteModel(
            name='HotDrinks',
        ),
        migrations.DeleteModel(
            name='Sandwich',
        ),
    ]
