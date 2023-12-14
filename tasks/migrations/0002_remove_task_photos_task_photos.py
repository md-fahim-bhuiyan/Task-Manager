# Generated by Django 5.0 on 2023-12-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='photos',
        ),
        migrations.AddField(
            model_name='task',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='task_photos/'),
        ),
    ]
