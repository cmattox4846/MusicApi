# Generated by Django 3.2.8 on 2021-11-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
