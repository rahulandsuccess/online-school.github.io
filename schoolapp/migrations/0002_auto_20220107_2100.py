# Generated by Django 3.2.9 on 2022-01-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attendence',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]