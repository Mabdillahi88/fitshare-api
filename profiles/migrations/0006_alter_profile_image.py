# Generated by Django 4.2.17 on 2025-01-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile.jpg', upload_to='images/'),
        ),
    ]
