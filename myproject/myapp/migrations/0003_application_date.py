# Generated by Django 5.1.3 on 2025-02-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_application_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Дата'),
        ),
    ]
