# Generated by Django 2.2.19 on 2021-03-08 16:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("pagesapp", "0005_fill_db"), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Basket",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="количество")),
                ("add_datetime", models.DateTimeField(auto_now_add=True, verbose_name="время добавления")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="pagesapp.Product")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="basket", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        )
    ]
