from django.db import models
from django.urls import reverse


class Music(models.Model):
    name = models.CharField(max_length=512)
    artist = models.CharField(max_length=512)
    lyrics = models.TextField()
    album_cover = models.URLField(max_length=1024, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk}) + '?pitch_id=%s' % '1'


    def __str__(self):
        return self.name

class Chord(models.Model):
    name = models.CharField(max_length=512)

    music = models.ForeignKey('Music',
                                  related_name='chord_music',
                                  on_delete=models.CASCADE)

    woman_chord_whether = models.BooleanField()
    man_chord_whether = models.BooleanField()
    youtube_embedded_source = models.CharField(max_length=5012)
    youtube_url = models.URLField(max_length=5012)

    pitch = models.ForeignKey('Pitch',
                                  related_name='chord_pitch',
                                  on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.music.name +'_' +  self.name + '_코드'


class Pitch(models.Model):

    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name