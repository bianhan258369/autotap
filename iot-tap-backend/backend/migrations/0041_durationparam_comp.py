# Generated by Django 2.0.2 on 2018-07-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0040_auto_20180727_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='durationparam',
            name='comp',
            field=models.BooleanField(default=False),
        ),
    ]
