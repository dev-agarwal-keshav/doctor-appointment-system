# Generated by Django 3.0.2 on 2020-06-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0009_schedule_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]