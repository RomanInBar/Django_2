# Generated by Django 2.2.12 on 2021-04-01 14:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0002_auto_20210331_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 14, 32, 20, 850905, tzinfo=utc)),
        ),
    ]