# Generated by Django 4.2.7 on 2023-11-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_profile_delete_aboutpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('icon', models.ImageField(upload_to='icons/')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='social_links',
            field=models.ManyToManyField(to='App.sociallink'),
        ),
    ]