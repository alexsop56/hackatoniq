# Generated by Django 5.0.7 on 2024-08-04 08:37

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('workersRequiredCount', models.IntegerField()),
                ('attentionCount', models.IntegerField()),
                ('todoCount', models.IntegerField()),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('inn', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('rating', models.FloatField()),
            ],
            options={
                'db_table': 'worker',
            },
        ),
        migrations.CreateModel(
            name='WorkerTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('workersCount', models.IntegerField()),
                ('workersRequiredCount', models.IntegerField()),
                ('views', models.IntegerField()),
                ('workTypeTitle', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='worker_shifts.project')),
                ('workers', models.ManyToManyField(related_name='shifts', to='worker_shifts.worker')),
            ],
            options={
                'db_table': 'worker_task',
            },
        ),
    ]