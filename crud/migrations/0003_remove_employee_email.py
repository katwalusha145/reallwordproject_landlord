# Generated by Django 3.0.2 on 2020-08-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_remove_employee_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
    ]