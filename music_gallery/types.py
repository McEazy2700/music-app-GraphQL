import graphene
from graphene_django import DjangoObjectType

from .models import Album, Genre, Artist, Song


class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = {
            "title": ("icontains", "istartswith", "exact"),
        }
        interfaces = (graphene.relay.Node,)


class ArtistNode(DjangoObjectType):
    class Meta:
        model = Artist
        filter_fields = {"name": ["icontains", "istartswith", "exact"]}
        interfaces = (graphene.relay.Node,)


class AlbumNode(DjangoObjectType):
    class Meta:
        model = Album
        filter_fields = {
            "id": ["exact"],
            "title": ["icontains", "istartswith", "exact"],
            "artist__name": ["icontains", "istartswith"],
            "artist__id": ["exact"],
            "genre__id": ["exact"],
        }
        interfaces = (graphene.relay.Node,)


class SongNode(DjangoObjectType):
    url = graphene.String(required=True)
    class Meta:
        model = Song
        filter_fields = {
            "id": ["exact"],
            "title": ["icontains", "istartswith"],
            "genre__title": ["icontains", "istartswith"],
            "artist__name": ["icontains", "istartswith"],
            "featured_artist__name": ["icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)

    def resolve_url(root, info, **kwargs):
        return root.get_music_url
