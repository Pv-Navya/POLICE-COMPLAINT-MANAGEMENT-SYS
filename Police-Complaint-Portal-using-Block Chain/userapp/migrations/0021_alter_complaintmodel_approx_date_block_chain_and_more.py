# Generated by Django 4.0.5 on 2022-12-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0020_complaintmodel_approx_date_block_chain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintmodel',
            name='Approx_date_block_chain',
            field=models.CharField(help_text='Approx_date_block_chain', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complaintmodel',
            name='Complaint_type_block_chain',
            field=models.CharField(help_text='Complaint_type_block_chain', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complaintmodel',
            name='occured_place_block_chain',
            field=models.CharField(help_text='occured_place_block_chain', max_length=100, null=True),
        ),
    ]
