from django import forms
from .models import MusicRequest

class MusicRequestForm(forms.ModelForm):
    class Meta:
        model = MusicRequest
        fields = ['audio_file', 'skill_level']