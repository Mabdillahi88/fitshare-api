# Generated by Django 4.2.17 on 2025-01-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dffdb3kza/image/upload/v1736357553/default_profile_wnsifs.jpg', upload_to='images/'),
        ),
    ]
