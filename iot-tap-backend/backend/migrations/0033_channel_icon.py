# Generated by Django 2.0.2 on 2018-07-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_auto_20180716_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='icon',
            field=models.TextField(null=True),
        ),
    ]
