# Generated by Django 3.1.5 on 2021-03-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zestapi', '0002_auto_20210307_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='ressource_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
