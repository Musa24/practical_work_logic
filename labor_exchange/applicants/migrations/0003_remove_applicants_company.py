# Generated by Django 3.1.7 on 2021-04-06 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_applicants_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicants',
            name='company',
        ),
    ]
