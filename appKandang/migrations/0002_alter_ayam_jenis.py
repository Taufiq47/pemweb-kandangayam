# Generated by Django 5.1.3 on 2024-12-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKandang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayam',
            name='jenis',
            field=models.CharField(choices=[('petelur', 'Petelur'), ('pedaging', 'Pedaging')], max_length=50),
        ),
    ]