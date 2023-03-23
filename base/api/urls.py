from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('songs/', views.getSongs),
    path('songs/<str:pk>/', views.getSong),
    path('artists/', views.getArtists),
    path('artists/<str:pk>/', views.getArtist),
]