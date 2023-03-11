from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('song/<str:pk>/', views.song_page, name="song"),
    path('add-song/', views.createLyricPage, name="add-song"),
    path('edit-song/<str:pk>/', views.editLyrics, name="edit-song"),
    path('delete-song/<str:pk>/', views.deleteSong, name="delete-song"),
    path('delete-comment/<str:pk>/', views.deleteComment, name="delete-comment"),
    path('rate/<str:pk>/<int:rating>/', views.rate, name="rate"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path("<str:pk>/followers/add", views.add_follower, name="add-follower"),
    path("<str:pk>/followers/remove", views.remove_follower, name="remove-follower"),
    path("favorite/<str:pk>/", views.favorite_song, name="favorite"),
    path("favorites/", views.song_favorites_list, name="favorite-songs-list"),
    path("<str:pk>/following", views.following, name="following"),
    path("artists-index/<str:letter>", views.artists_index, name="artists-index"),
    path("artists/<str:artist>", views.artist_page, name="artists-page"),
    path("edit-request/<str:pk>", views.edit_request, name="edit-request"),
    path("requests", views.requests, name="requests"),
    path("request/<str:pk>", views.request_view, name="request-view"),
    path("approve-request/<str:pk>", views.approve_request, name="approve-request"),
    path("deny-request/<str:pk>", views.deny_request, name="deny-request"),
    path("update-user/", views.updateUser, name="update-user"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]