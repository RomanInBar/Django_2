# Generated by Django 2.2.12 on 2021-04-05 17:00

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0007_auto_20210402_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 17, 0, 19, 167624, tzinfo=utc)),
        ),
    ]
