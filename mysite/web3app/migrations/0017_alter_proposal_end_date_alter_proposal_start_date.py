# Generated by Django 4.0.4 on 2022-06-13 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web3app', '0016_alter_proposal_end_date_alter_proposal_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 23, 3, 59, 704414)),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 23, 3, 59, 703416)),
        ),
    ]
