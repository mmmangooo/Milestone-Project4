# Generated by Django 3.2.2 on 2021-05-16 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_auto_20210512_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='toy',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign', to='toys.campaign'),
        ),
    ]
