# Generated by Django 3.2.8 on 2021-11-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
