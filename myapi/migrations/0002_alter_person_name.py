# Generated by Django 4.2.5 on 2023-09-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]