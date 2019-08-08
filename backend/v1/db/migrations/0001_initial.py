# Generated by Django 2.2.4 on 2019-08-04 16:36

import django.core.validators
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing_id', models.CharField(max_length=24, validators=[django.core.validators.MinLengthValidator(24)])),
                ('data', django_mysql.models.JSONField(default=dict)),
                ('schema', django_mysql.models.JSONField(default=dict)),
                ('user_agent', models.CharField(blank=True, max_length=256)),
                ('ip_v4_address', models.CharField(blank=True, max_length=19, validators=[django.core.validators.MinLengthValidator(19)])),
                ('registered_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'landing_page_db',
            },
        ),
    ]