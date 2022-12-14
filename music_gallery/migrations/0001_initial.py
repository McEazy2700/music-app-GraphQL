# Generated by Django 3.2.15 on 2022-09-15 08:27

import cloudinary_storage.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_photo', models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage, upload_to='uploads/albums')),
                ('date_added', models.DateTimeField(editable=False)),
                ('last_updated', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage, upload_to='uploads/artists')),
                ('date_added', models.DateTimeField(editable=False)),
                ('last_updated', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('date_added', models.DateTimeField(editable=False)),
                ('last_updated', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.FileField(blank=True, null=True, upload_to='uploads/songs')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_photo', models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage, upload_to='uploads/songs/images')),
                ('date_added', models.DateTimeField(editable=False)),
                ('last_updated', models.DateTimeField(editable=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_gallery.album')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='songs', to='music_gallery.artist')),
                ('featured_artist', models.ManyToManyField(blank=True, to='music_gallery.Artist')),
                ('genre', models.ManyToManyField(blank=True, to='music_gallery.Genre')),
                ('music', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music_gallery.music')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='albums', to='music_gallery.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='featured_artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_gallery.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(blank=True, to='music_gallery.Genre'),
        ),
    ]
