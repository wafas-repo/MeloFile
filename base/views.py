from django.shortcuts import render, redirect
from django.db.models import Q
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import Song, Genre, Comment, User, Rating, Artist
from . forms import SongForm


# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    songs =  Song.objects.filter(
        Q(title__icontains=q) |
        Q(genre__name__icontains=q) | 
        Q(artist__name__icontains=q)
        )
    genres= Genre.objects.all()
    latest = Song.objects.all()[::-1][0:5]
    ratings = Song.objects.annotate(avg_rate=(Avg("rating__rating"))).order_by('avg_rate')[::-1][:5]
    context = {'songs': songs, 'genres': genres, 'latest':latest, 'ratings': ratings}
    return render(request, 'base/home.html', context )

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    songs = user.song_set.all()
    # comments = user.comment_set.all()
    # genres = Genre.objects.all()

    followers = user.followers.all()
    following = user.following.all()
    if len(followers) == 0:
        is_following = False

    for follower in followers:
        if follower == request.user:
            is_following = True
        else:
            is_following = False

    num_followers = len(followers)
    number_of_following = len(following)

    context = {
        'user':user, 
        'songs': songs, 
        'is_following': is_following, 
        'num_followers': num_followers,
        "num_following": number_of_following
        }
    return render(request, 'base/profile.html', context)

def song_page(request, pk):
    song =  Song.objects.get(id=pk)
    comments = song.comments.all().order_by('-date_added')
    contributors = song.contributors.all()
    song.contributors.add(song.creator)
    ratings = Rating.objects.filter(song=song)
    rating = Rating.objects.filter(song=song, user=request.user).first()
    song.user_rating = rating.rating if rating else 0
    rating_count = ratings.count()
    is_favorite = False
    if song.favorite.filter(id=request.user.id).exists():
        is_favorite = True
    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            song=song,
            comment=request.POST.get('comment')
        )
        return redirect('song', pk=song.id)
    context = {'song': song, 'comments':comments, 'contributors':contributors, 'rating_count':rating_count, 'is_favorite': is_favorite }
    return render(request, 'base/song.html', context)

def createLyricPage(request):
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.creator = request.user
            song.save()
            return redirect('home')

    context = {'form':form}
    return render(request, "base/song_form.html", context)

def favorite_song(request, pk):
    song = Song.objects.get(id=pk)
    if song.favorite.filter(pk=request.user.id).exists():
        song.favorite.remove(request.user)
    else:
        song.favorite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def song_favorites_list(request):
    user = request.user
    favorite_songs = user.favorite.all()
    context = {
        'favorite_songs':favorite_songs
    }
    return render(request, 'base/favorite_songs.html', context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "base/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "base/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "base/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "base/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "base/register.html")


def editLyrics(request, pk):
    song = Song.objects.get(id=pk)
    form = SongForm(instance=song)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, "base/song_form.html", context)

def deleteSong(request, pk):
    song = Song.objects.get(id=pk)

    if request.user != song.creator:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        song.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': song})

def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': comment})

def rate(request, pk, rating):
    song = Song.objects.get(id=pk)
    Rating.objects.filter(song=song, user=request.user).delete()
    song.ratings.create(user=request.user, rating=rating)
    return render(request, 'base/song.html')

def add_follower(request, pk):
    profile = User.objects.get(id=pk)
    profile.followers.add(request.user)
    curr_user = User.objects.get(id=request.user.id)
    curr_user.following.add(profile)
    return redirect('user-profile', profile.id)

def remove_follower(request, pk):
    profile = User.objects.get(id=pk)
    profile.followers.remove(request.user)
    curr_user = User.objects.get(id=request.user.id)
    curr_user.following.remove(profile)

    return redirect('user-profile', profile.id)
   
def following(request, pk):
    uid = User.objects.get(id=pk)
    following = uid.following.all()
    songs = Song.objects.filter(creator__in=following).order_by('-created')
    following_comments = Comment.objects.filter(user__in=following).order_by('-date_added')

    return render(request, "base/following.html", {
        "songs":songs,
        "following_comments": following_comments
    })