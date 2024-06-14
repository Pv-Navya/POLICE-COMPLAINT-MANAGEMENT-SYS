# Generated by Django 4.1.4 on 2022-12-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_complaintmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('star', models.IntegerField()),
                ('comment', models.CharField(help_text='comment', max_length=500)),
            ],
            options={
                'db_table': 'user_comments',
            },
        ),
    ]
