# Generated by Django 4.2.17 on 2025-03-27 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='title',
            field=models.CharField(choices=[('NEWBIE', 'Newbie'), ('POPULAR_POST', 'Popular Post'), ('COMMENT_CHAMPION', 'Comment Champion')], default='NEWBIE', max_length=50),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
