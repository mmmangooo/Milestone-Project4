# Generated by Django 3.2.2 on 2021-05-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_auto_20210516_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='toys'),
        ),
    ]