# Generated by Django 2.1.7 on 2019-04-07 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0004_auto_20190317_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='intensoferta',
            name='ordem',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oferta',
            name='datafim',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 7, 15, 48, 24, 514554)),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='datainicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 7, 15, 48, 24, 514554)),
        ),
    ]
