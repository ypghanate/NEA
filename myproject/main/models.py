from django.db import models


class MusicRequest(models.Model):
    SKILL_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ]

    audio_file = models.FileField(upload_to='uploads/audio/')
    skill_level = models.CharField(max_length=10, choices=SKILL_LEVELS)

    midi_file = models.FileField(upload_to='uploads/midi/', null=True, blank=True)
    sheet_music = models.FileField(upload_to='uploads/sheet_music/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.skill_level} - {self.audio_file.name}"

