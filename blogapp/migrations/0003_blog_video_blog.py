# Generated by Django 3.2.9 on 2021-11-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20211108_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video_blog',
            field=models.FileField(blank=True, null=True, upload_to='my_videos'),
        ),
    ]
