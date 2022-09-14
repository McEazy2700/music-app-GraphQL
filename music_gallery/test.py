from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    date_added = models.DateTimeField(editable=False)
    last_updated = models.DateTimeField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = timezone.now()
        self.last_updated = timezone.now()
        return super(Genre, self).save(*args, **kwargs)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/artists", null=True, blank=True)
    date_added = models.DateTimeField(editable=False)
    last_updated = models.DateTimeField(editable=False)

    def __str__(self):
        return self.name

    
    @property
    def get_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return None

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = timezone.now()
        self.last_updated = timezone.now()
        return super(Artist, self).save(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=255)
    cover_photo = models.ImageField(upload_to="uploads/albums", null=True, blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.PROTECT, related_name="albums", null=True, blank=True
    )
    genre = models.ManyToManyField(Genre, blank=True)
    featured_artist = models.ForeignKey(
        Artist, on_delete=models.PROTECT, null=True, blank=True
    )
    date_added = models.DateTimeField(editable=False)
    last_updated = models.DateTimeField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = timezone.now()
        self.last_updated = timezone.now()
        return super(Album, self).save(*args, **kwargs)

    @property
    def get_url(self):
        if self.cover_photo and hasattr(self.cover_photo, 'url'):
            return self.cover_photo.url
        return None


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, null=True, blank=True)
    music = models.FileField(upload_to="uploads/songs")
    genre = models.ManyToManyField(Genre, blank=True)
    cover_photo = models.ImageField(upload_to='uploads/songs/images', null=True, blank=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.PROTECT, related_name="songs", null=True, blank=True
    )
    featured_artist = models.ManyToManyField(Artist, blank=True)
    date_added = models.DateTimeField(editable=False)
    last_updated = models.DateTimeField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = timezone.now()
        self.last_updated = timezone.now()
        return super(Song, self).save(*args, **kwargs)

    @property
    def get_url(self):
        if self.cover_photo and hasattr(self.cover_photo, 'url'):
            return self.cover_photo.url
        return None


