# Generated by Django 4.2 on 2023-12-21 07:34

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_group_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
            ],
            options={
                'verbose_name': 'Roles',
                'verbose_name_plural': 'Roles',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users', verbose_name='image')),
                ('description', models.TextField(help_text='description for any user', null=True, verbose_name='description')),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='user/cv', verbose_name='cv file')),
                ('ns_image', models.ImageField(blank=True, null=True, upload_to='user/national_card', verbose_name='national card image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]