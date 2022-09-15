# Generated by Django 3.2.15 on 2022-09-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song',
            field=models.FileField(blank=True, null=True, upload_to='uploads/songs'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
