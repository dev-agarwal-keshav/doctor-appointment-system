# Generated by Django 3.0.2 on 2020-06-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='patient',
            name='patId',
            field=models.TextField(default='', primary_key=True, serialize=False),
        ),
    ]
