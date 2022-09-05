import graphene
from music_gallery.queries import GalleryQuery


class Query(GalleryQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)