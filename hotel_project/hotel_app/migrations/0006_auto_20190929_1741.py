# Generated by Django 2.0 on 2019-09-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0005_auto_20190929_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomments',
            name='customer_name',
            field=models.CharField(max_length=100),
        ),
    ]
