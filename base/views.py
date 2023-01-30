from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import Song, Genre
from . forms import SongForm


# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    songs =  Song.objects.filter(
        Q(title__icontains=q) |
        Q(genre__name__icontains=q) | 
        Q(artist__icontains=q)
        )
    genres= Genre.objects.all()
    context = {'songs': songs, 'genres': genres}
    return render(request, 'base/home.html', context )

def song_page(request, pk):
    song =  Song.objects.get(id=pk)
    context = {'song': song}
    return render(request, 'base/song.html', context)

def createLyricPage(request):
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, "base/song_form.html", context)

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