# Generated by Django 4.2.3 on 2023-07-28 14:38

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarCategorie',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('categorie', models.CharField(choices=[('SEDAN', 'SEDAN'), ('WORK_VAN', 'WORK VAN')], max_length=30, unique=True)),
                ('value', models.FloatField()),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('chassis_number', models.CharField(max_length=17, unique=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('manufacture_year', models.DateTimeField()),
                ('model_year', models.DateTimeField()),
                ('mileage', models.FloatField()),
                ('car_plate', models.CharField(max_length=7, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(choices=[('ELECTRIC_VEHICLE', 'ELECTRIC VEHICLE')], max_length=30)),
                ('fuel_level', models.CharField(choices=[('FULL', 'FULL')], max_length=30)),
                ('status', models.CharField(default='VACANT', max_length=10)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carcategorie')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
