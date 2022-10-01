import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .types import AlbumNode, ArtistNode, GenreNode, SongNode

class GalleryQuery(graphene.ObjectType):
    all_songs = DjangoFilterConnectionField(SongNode)
    all_artists = DjangoFilterConnectionField(ArtistNode)
    all_genres = DjangoFilterConnectionField(GenreNode)
    all_albums = DjangoFilterConnectionField(AlbumNode)
