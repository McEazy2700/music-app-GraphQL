from django.contrib import admin
from .models import (
    Album, Artist, Genre, Song
)
# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_added']
    list_filter = ['artist', 'genre']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_added']
    list_filter = ['name']


@admin.register(Genre)
class GereAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_added']
    list_filter = ['title']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_added']
    list_filter = ['genre', 'date_added']
