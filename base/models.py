from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg
# Create your models here.

class User(AbstractUser):
    # avatar = models.ImageField()
    follower = models.ManyToManyField('self', blank=True, symmetrical=False,  related_name='followers')
    follow = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='following')

    # def count_followers(self):
    #     return self.followers.count()
    
    # def count_following(self):
    #     return User.objects.filter(followers=self).count()
    

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    lyrics = models.TextField(null=False, blank=False)
    contributors = models.ManyToManyField(User, related_name='contributors', blank=True)
    genre = models.ManyToManyField(Genre)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True,null=True)
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)

    def average_rating(self) -> float:
        return Rating.objects.filter(song=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.song.title, self.user)# pylint: disable=maybe-no-member

class Rating(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.song.title}: {self.rating}"

class EditRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default=None)
    edit = models.TextField(default=None)
    pending = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'from: %s - to: %s' % (self.from_user.username, self.to_user.username)

