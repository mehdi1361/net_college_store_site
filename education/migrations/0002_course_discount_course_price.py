# Generated by Django 4.2.7 on 2023-11-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="discount",
            field=models.PositiveIntegerField(default=0, verbose_name="discount"),
        ),
        migrations.AddField(
            model_name="course",
            name="price",
            field=models.PositiveIntegerField(default=0, verbose_name="price"),
        ),
    ]