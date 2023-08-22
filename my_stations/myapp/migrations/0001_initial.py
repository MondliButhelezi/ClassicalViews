# Generated by Django 4.2.4 on 2023-08-22 07:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('last_update', models.DateTimeField()),
                ('last_update_by', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitoringStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('last_update', models.DateTimeField()),
                ('last_update_by', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('equipment_type_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitoring_units', to='myapp.equipmenttype')),
            ],
        ),
    ]
