from django.contrib import admin

from .models import Music, Chord, Pitch

admin.site.register(Music)
admin.site.register(Chord)
admin.site.register(Pitch)