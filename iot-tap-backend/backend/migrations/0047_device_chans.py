# Generated by Django 2.0.2 on 2018-08-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0046_auto_20180731_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='chans',
            field=models.ManyToManyField(to='backend.Channel'),
        ),
    ]
