# Generated by Django 4.2.16 on 2024-10-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wear_and_share", "0002_remove_customuser_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="costume",
            name="category",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="costume",
            name="size",
            field=models.CharField(max_length=1),
        ),
    ]