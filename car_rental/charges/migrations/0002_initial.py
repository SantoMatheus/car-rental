# Generated by Django 4.2.3 on 2023-09-15 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rents', '0001_initial'),
        ('charges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rents.rent'),
        ),
    ]