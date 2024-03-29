# Generated by Django 5.0.1 on 2024-01-29 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=6)])),
                ('conform_password', models.CharField(max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=6)])),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
            ],
        ),
    ]
