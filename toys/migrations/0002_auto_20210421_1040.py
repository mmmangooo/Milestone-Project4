# Generated by Django 3.2 on 2021-04-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='toy',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
