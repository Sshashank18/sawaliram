# Generated by Django 2.2.3 on 2020-02-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sawaliram_auth', '0014_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verification_code_expiry',
            field=models.DateTimeField(null=True),
        ),
    ]