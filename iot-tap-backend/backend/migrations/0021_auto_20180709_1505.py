# Generated by Django 2.0.2 on 2018-07-09 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_auto_20180708_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinCap',
            fields=[
                ('capability_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Capability')),
                ('tval', models.TextField()),
                ('fval', models.TextField()),
            ],
            bases=('backend.capability',),
        ),
        migrations.CreateModel(
            name='RangeCap',
            fields=[
                ('capability_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Capability')),
                ('min', models.IntegerField()),
                ('max', models.IntegerField()),
            ],
            bases=('backend.capability',),
        ),
        migrations.CreateModel(
            name='SetCap',
            fields=[
                ('capability_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Capability')),
                ('numopts', models.IntegerField()),
            ],
            bases=('backend.capability',),
        ),
        migrations.CreateModel(
            name='SetCapOpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.SetCap')),
            ],
        ),
        migrations.RemoveField(
            model_name='stateval',
            name='cap',
        ),
        migrations.RemoveField(
            model_name='capability',
            name='range_max',
        ),
        migrations.RemoveField(
            model_name='capability',
            name='range_min',
        ),
        migrations.RemoveField(
            model_name='statelog',
            name='state',
        ),
        migrations.AddField(
            model_name='statelog',
            name='cap',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='logcap', to='backend.Capability'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statelog',
            name='dev',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='logdev', to='backend.Capability'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statelog',
            name='value',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='capability',
            name='statelabel',
            field=models.TextField(default="$$DEVICE$$'s $$CAPNAME$$ is $$STATE$$", null=True),
        ),
        migrations.AlterField(
            model_name='capability',
            name='type',
            field=models.TextField(choices=[('set', 'Set'), ('range', 'Range'), ('bin', 'Binary'), ('hist', 'History')]),
        ),
        migrations.AlterField(
            model_name='state',
            name='value',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='StateVal',
        ),
    ]
