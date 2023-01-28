from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('song/<str:pk>/', views.song_page, name="song"),
    path('add-song/', views.createLyricPage, name="add-song"),



    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]