# Generated by Django 4.1 on 2022-10-17 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appweb', '0002_alter_cartas_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprador',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254),
            preserve_default=False,
        ),
    ]