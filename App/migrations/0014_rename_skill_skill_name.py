# Generated by Django 4.2.7 on 2023-11-28 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_rename_skill_profile_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='name',
        ),
    ]
