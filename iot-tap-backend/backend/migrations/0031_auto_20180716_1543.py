# Generated by Django 2.0.2 on 2018-07-16 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_auto_20180716_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='esrule',
            name='id',
        ),
        migrations.RemoveField(
            model_name='esrule',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='ssrule',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ssrule',
            name='owner',
        ),
        migrations.AddField(
            model_name='esrule',
            name='rule_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Rule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ssrule',
            name='rule_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Rule'),
            preserve_default=False,
        ),
    ]
