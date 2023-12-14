# Generated by Django 3.2 on 2023-11-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_data', '0002_coursecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='color',
            field=models.CharField(choices=[('cat-1', 'cat-1'), ('cat-2', 'cat-2'), ('cat-3', 'cat-3'), ('cat-4', 'cat-4'), ('cat-10', 'cat-10'), ('cat-6', 'cat-6'), ('cat-7', 'cat-7'), ('cat-8', 'cat-8'), ('cat-9', 'cat-9')], max_length=100, verbose_name='COLOR'),
        ),
    ]
