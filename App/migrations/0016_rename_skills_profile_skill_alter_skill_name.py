# Generated by Django 4.2.7 on 2023-11-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_skill_description_alter_skill_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='skills',
            new_name='skill',
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
