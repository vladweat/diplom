# Generated by Django 4.0.4 on 2022-06-13 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web3app', '0010_votingvoters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='end_date',
            field=models.DateTimeField(verbose_name=models.DateTimeField(blank=True, default=datetime.datetime.now)),
        ),
    ]
