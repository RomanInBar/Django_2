# Generated by Django 2.2.12 on 2021-04-02 16:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0006_auto_20210401_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 16, 5, 11, 486835, tzinfo=utc)),
        ),
    ]
