# Generated by Django 3.2.18 on 2023-02-15 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_photo_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='type',
        ),
    ]
