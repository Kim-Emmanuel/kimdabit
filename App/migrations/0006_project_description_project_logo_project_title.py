# Generated by Django 4.2.7 on 2023-11-23 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
