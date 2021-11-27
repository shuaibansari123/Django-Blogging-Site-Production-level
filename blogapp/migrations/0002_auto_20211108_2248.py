# Generated by Django 3.2.9 on 2021-11-08 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='pera_2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='pera_3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='pera_4',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_4',
        ),
        migrations.AddField(
            model_name='blog',
            name='like_blog',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_by',
            field=models.ForeignKey(default='Anonymos', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unique_user',
            name='unique',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
