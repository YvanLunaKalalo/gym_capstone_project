# Generated by Django 4.2.15 on 2024-10-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0009_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='progress_date',
            field=models.DateField(auto_now=True),
        ),
    ]
