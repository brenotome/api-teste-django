# Generated by Django 3.0.2 on 2020-02-08 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200208_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='creation_date',
            new_name='date',
        ),
    ]