# Generated by Django 4.2.7 on 2023-11-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_blog_photo_project_sociallink_profile_social_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]