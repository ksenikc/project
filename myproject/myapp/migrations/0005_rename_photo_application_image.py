# Generated by Django 5.1.3 on 2025-02-15 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_application_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='photo',
            new_name='image',
        ),
    ]
