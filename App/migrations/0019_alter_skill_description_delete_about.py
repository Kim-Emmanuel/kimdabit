# Generated by Django 4.2.7 on 2023-11-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]