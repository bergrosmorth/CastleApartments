# Generated by Django 2.2.1 on 2019-05-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0007_auto_20190517_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhouse',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='openhouse',
            name='time',
            field=models.CharField(max_length=15),
        ),
    ]