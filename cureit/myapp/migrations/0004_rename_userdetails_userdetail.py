# Generated by Django 4.0.3 on 2022-05-12 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_employee_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]
