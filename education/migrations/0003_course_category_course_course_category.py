# Generated by Django 4.2.7 on 2023-11-19 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("site_data", "0003_alter_coursecategory_color"),
        ("education", "0002_course_discount_course_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="site_data.category",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="course_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="site_data.coursecategory",
            ),
        ),
    ]
