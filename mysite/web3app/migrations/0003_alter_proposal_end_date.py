# Generated by Django 4.0.4 on 2022-05-22 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web3app', '0002_alter_proposal_description_alter_proposal_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]