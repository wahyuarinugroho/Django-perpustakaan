# Generated by Django 3.2.2 on 2021-10-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_auto_20211027_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='kelompok',
            name='keterangan',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='kelompok',
            name='nama',
            field=models.CharField(max_length=10),
        ),
    ]
