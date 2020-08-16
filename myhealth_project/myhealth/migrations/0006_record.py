# Generated by Django 2.2.2 on 2020-08-13 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhealth', '0005_delete_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sympton', models.TextField(null=True)),
                ('treatment', models.TextField(null=True)),
                ('prescription', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('allowed_users', models.ManyToManyField(related_name='allowed_users', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_doctor_id', to='myhealth.DoctorProfile')),
                ('doctor_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_email', to=settings.AUTH_USER_MODEL)),
                ('patient_gpno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_patient_gpno', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]