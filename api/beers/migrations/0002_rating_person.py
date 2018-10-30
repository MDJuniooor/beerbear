# Generated by Django 2.1.2 on 2018-10-29 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='person',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
