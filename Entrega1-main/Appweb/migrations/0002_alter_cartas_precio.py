# Generated by Django 4.1 on 2022-09-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartas',
            name='precio',
            field=models.FloatField(),
        ),
    ]
