# Generated by Django 2.1.2 on 2018-10-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0002_rating_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='ABV',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='avg_scr',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='brewery',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='style',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
