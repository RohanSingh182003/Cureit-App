# Generated by Django 4.0.3 on 2022-05-14 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_stress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stress',
            old_name='q10',
            new_name='result',
        ),
    ]
