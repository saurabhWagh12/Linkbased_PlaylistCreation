from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',loginForm,name="LoggingIn"),
    path('home/',home,name="Home"),
    path('register/',register,name="Registration"),
    path('logout/',loggingOut,name="LoggingOut"),
    path('playlist/<str:id>/',intoPlayList,name="OpenedPlaylist"),
    path('favourites/',viewFavs,name="Favourites"),
    path('addplaylist/',addPlaylist,name="AddPlaylist"),
    path('deleteplaylist/<str:id>/',deletePlayList,name="Deleting-Playlist"),
    path('addItem/<str:id>/',addItem,name="AddingItem"),
    path('add/<str:id>/',add,name="Adding"),
    path('deletevideo/<str:id>/<str:idp>/',deleteVideo,name="deleting-video"),
]
