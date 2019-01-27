# Generated by Django 2.0.2 on 2018-06-12 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_better_ssrule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capability',
            name='channel',
        ),
        migrations.AddField(
            model_name='capability',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.Channel'),
        ),
    ]
