# Generated by Django 4.2.3 on 2023-08-11 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myplaylist',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
