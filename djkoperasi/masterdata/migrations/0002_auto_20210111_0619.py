# Generated by Django 2.2.7 on 2021-01-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='possaldo',
            field=models.IntegerField(choices=[('debet', 'Debet'), ('kredit', 'Kredit')], max_length=2, verbose_name='PosSaldo*'),
        ),
    ]
