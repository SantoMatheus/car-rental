# Generated by Django 4.2.3 on 2023-07-28 02:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_plate',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]