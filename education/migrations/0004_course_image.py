# Generated by Django 4.2.7 on 2023-11-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0003_course_category_course_course_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="image",
            field=models.ImageField(
                null=True, upload_to="course", verbose_name="image"
            ),
        ),
    ]
