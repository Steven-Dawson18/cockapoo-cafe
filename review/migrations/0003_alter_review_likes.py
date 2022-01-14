# Generated by Django 3.2.9 on 2022-01-12 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0002_review_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]