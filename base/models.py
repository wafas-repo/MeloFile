from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=20)
    lyrics = models.TextField(null=False, blank=False)
    genre = models.ManyToManyField(Genre)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.song.title, self.user)# pylint: disable=maybe-no-member

# Rating

# Artist (Maybe)