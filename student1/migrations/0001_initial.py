# Generated by Django 4.1.3 on 2022-11-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stuname", models.CharField(max_length=40)),
                ("stuage", models.IntegerField()),
                ("sturno", models.IntegerField()),
            ],
        ),
    ]
