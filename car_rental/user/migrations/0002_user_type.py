# Generated by Django 4.2.3 on 2023-07-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('CPF', 'CPF'), ('CNPJ', 'CNPJ')], default=2, max_length=4),
            preserve_default=False,
        ),
    ]