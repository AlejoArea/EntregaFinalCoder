# Generated by Django 4.1 on 2022-10-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appweb', '0011_alter_cartas_rareza'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartas',
            name='costo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartas',
            name='tipo',
            field=models.CharField(default='spell', max_length=20),
            preserve_default=False,
        ),
    ]
