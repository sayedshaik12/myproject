# Generated by Django 3.2.14 on 2022-08-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.CharField(default='any topic', max_length=100),
        ),
    ]
