# Generated by Django 2.2.28 on 2022-10-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_usertest"),
    ]

    operations = [
        migrations.CreateModel(
            name="Addeddata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("himanshu", models.BigIntegerField()),
            ],
        ),
    ]
