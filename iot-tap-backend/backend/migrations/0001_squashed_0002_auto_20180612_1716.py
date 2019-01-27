# Generated by Django 2.0.2 on 2018-06-12 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('backend', '0001_initial'), ('backend', '0002_auto_20180612_1716')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('changeable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capabilities', models.ManyToManyField(to='backend.Capability')),
            ],
        ),
        migrations.CreateModel(
            name='ESRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actioncap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ESactioncap', to='backend.Capability')),
                ('actiondev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ESactiondev', to='backend.Device')),
                ('triggercapE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EStriggercapE', to='backend.Capability')),
                ('triggercapS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EStriggercapS', to='backend.Capability')),
                ('triggerdevE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EStriggerdevE', to='backend.Device')),
                ('triggerdevS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EStriggerdevS', to='backend.Device')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('active', models.BooleanField()),
                ('cap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Capability')),
                ('dev', models.ForeignKey(default='yikes', on_delete=django.db.models.deletion.CASCADE, to='backend.Device')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='capability',
            name='channel',
            field=models.ManyToManyField(to='backend.Channel'),
        ),
        migrations.CreateModel(
            name='SSRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField()),
                ('actioncap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actioncap', to='backend.Capability')),
                ('actiondev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SSactiondev', to='backend.Device')),
                ('actionstate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionstate', to='backend.State')),
                ('trigger1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SStrigger1', to='backend.State')),
                ('trigger2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SStrigger2', to='backend.State')),
            ],
        ),
    ]
