# Generated by Django 3.2.14 on 2022-08-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20220820_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasave',
            name='email',
            field=models.EmailField(default='liveforothers@gmail.com', max_length=40),
        ),
    ]
