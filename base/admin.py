from django.contrib import admin
from .models import User, Song, Comment, Genre, Rating, Artist, EditRequest

# Register your models here.
admin.site.register(User)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Artist)
admin.site.register(EditRequest)
