# Generated by Django 2.2.12 on 2021-04-01 15:06

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0003_auto_20210401_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 15, 6, 38, 689130, tzinfo=utc)),
        ),
    ]
