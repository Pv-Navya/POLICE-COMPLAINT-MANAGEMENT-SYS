# Generated by Django 4.1.4 on 2022-12-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_alter_usermodel_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintModel',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('suspect_name', models.CharField(help_text='suspect_name', max_length=50)),
                ('Complaint_type', models.CharField(help_text='complaint_type', max_length=30)),
                ('Approx_date_time', models.DateField()),
                ('Evidence', models.FileField(upload_to='documents/')),
                ('occured_place', models.CharField(help_text='occured_place', max_length=100)),
                ('complaint_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_complaints',
            },
        ),
    ]
