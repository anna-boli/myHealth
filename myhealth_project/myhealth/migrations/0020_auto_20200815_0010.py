# Generated by Django 2.2.2 on 2020-08-14 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhealth', '0019_remove_reply_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='question',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='respondent',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
