# Generated by Django 3.1.5 on 2021-03-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zestapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='picture',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
