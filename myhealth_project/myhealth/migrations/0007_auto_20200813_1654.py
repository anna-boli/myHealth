# Generated by Django 2.2.2 on 2020-08-13 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhealth', '0006_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='patient_gpno',
            new_name='patient',
        ),
    ]