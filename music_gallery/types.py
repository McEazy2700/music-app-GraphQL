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
    artist_id = graphene.ID()
    photo_url = graphene.String()
    class Meta:
        model = Artist
        filter_fields = {"name": ["icontains", "istartswith", "exact"]}
        interfaces = (graphene.relay.Node,)

    def resolve_photo_url(self, info, **kwargs):
        return self.get_url

    def resolve_artist_id(self, info, **kwargs):
        return self.id


class AlbumNode(DjangoObjectType):
    album_id = graphene.ID()
    photo_url = graphene.String()
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

    def resolve_album_id(self, info, **kwargs):
        return self.id

    def resolve_photo_url(self, info, **kwargs):
        return self.get_url


class SongNode(DjangoObjectType):
    url = graphene.String(required=True)
    photo_url = graphene.String()
    class Meta:
        model = Song
        filter_fields = {
            "id": ["exact"],
            "title": ["icontains", "istartswith"],
            "genre__title": ["icontains", "istartswith"],
            "artist__name": ["icontains", "istartswith"],
            "album__id": ["exact"],
            "featured_artist__name": ["icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)

    def resolve_url(self, info, **kwargs):
        return self.get_music_url

    def resolve_photo_url(self, info, **kwargs):
        return self.get_image_url
