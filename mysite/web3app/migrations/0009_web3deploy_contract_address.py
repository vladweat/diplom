# Generated by Django 4.0.4 on 2022-06-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web3app', '0008_rename_creator_id_web3deploy_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='web3deploy',
            name='contract_address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
