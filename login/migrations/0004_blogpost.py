# Generated by Django 3.2.14 on 2022-08-21 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_datasave_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100000)),
                ('created_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
