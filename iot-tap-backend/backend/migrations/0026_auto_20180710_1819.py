# Generated by Django 2.0.2 on 2018-07-10 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_auto_20180710_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eerule',
            name='actionstate',
        ),
        migrations.RemoveField(
            model_name='eerule',
            name='triggers',
        ),
        migrations.RenameField(
            model_name='esrule',
            old_name='triggerE',
            new_name='Etrigger',
        ),
        migrations.RenameField(
            model_name='esrule',
            old_name='triggersS',
            new_name='Striggers',
        ),
        migrations.RenameField(
            model_name='esrule',
            old_name='actionstate',
            new_name='action',
        ),
        migrations.RenameField(
            model_name='ssrule',
            old_name='actionstate',
            new_name='action',
        ),
        migrations.AddField(
            model_name='state',
            name='param',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.Parameter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statelog',
            name='param',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='logparam', to='backend.Parameter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statelog',
            name='dev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logdev', to='backend.Device'),
        ),
        migrations.DeleteModel(
            name='EERule',
        ),
    ]
