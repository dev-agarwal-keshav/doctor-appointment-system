# Generated by Django 3.0.2 on 2020-06-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0010_auto_20200618_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=11),
        ),
    ]
