# Generated by Django 4.0.5 on 2022-12-15 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0018_usermodel_user_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='user_key',
        ),
    ]
