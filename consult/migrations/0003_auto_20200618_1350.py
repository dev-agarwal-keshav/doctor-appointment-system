# Generated by Django 3.0.2 on 2020-06-18 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_auto_20200618_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patId',
            new_name='patID',
        ),
    ]