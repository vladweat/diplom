# Generated by Django 4.0.4 on 2022-06-10 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web3app', '0007_web3deploy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='web3deploy',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='web3deploy',
            old_name='proposal_id',
            new_name='proposal',
        ),
    ]