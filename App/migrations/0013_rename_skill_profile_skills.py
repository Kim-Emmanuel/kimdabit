# Generated by Django 4.2.7 on 2023-11-28 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_skill_profile_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='skill',
            new_name='skills',
        ),
    ]
