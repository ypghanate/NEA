from django.contrib import admin
from .models import MusicRequest


@admin.register(MusicRequest)
class MusicRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_level', 'status', 'created_at')
    list_filter = ('skill_level', 'status')
    search_fields = ('audio_file', 'midi_file', 'sheet_music')
