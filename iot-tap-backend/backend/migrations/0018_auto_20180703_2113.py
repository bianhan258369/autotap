# Generated by Django 2.0.2 on 2018-07-03 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_statelog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='active',
        ),
        migrations.RemoveField(
            model_name='state',
            name='bi',
        ),
        migrations.AddField(
            model_name='state',
            name='valopts',
            field=models.TextField(default='On,Off'),
        ),
        migrations.AddField(
            model_name='state',
            name='valtype',
            field=models.TextField(default='set'),
        ),
    ]