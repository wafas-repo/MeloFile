# Generated by Django 4.0.6 on 2023-03-23 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_song_album_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album_art',
            field=models.URLField(default='https://cdn.lsistatic.com/img/no_img_artist.png'),
        ),
    ]