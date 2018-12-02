# Generated by Django 2.1.2 on 2018-11-25 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beershops', '0004_auto_20181125_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='beershop',
            name='favorite_user_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_beershop_list', to=settings.AUTH_USER_MODEL),
        ),
    ]