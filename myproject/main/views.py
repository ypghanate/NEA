from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import MusicRequest
from .forms import MusicRequestForm
from .backend_logic import audio_to_midi, convert_audio_sheet
import os

def upload_view(request):
    if request.method == 'POST':
        form = MusicRequestForm(request.POST, request.FILES)
        if form.is_valid():
            # Save initial MusicRequest
            music_request = form.save(commit=False)
            music_request.status = 'pending'
            music_request.save()

            audio_path = music_request.audio_file.path
            user_skill = form.cleaned_data.get('skill_level')

            # Ensure directories exist
            midi_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', 'midi')
            sheet_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', 'sheet_music')
            os.makedirs(midi_dir, exist_ok=True)
            os.makedirs(sheet_dir, exist_ok=True)

            # Convert audio to MIDI
            base_name = os.path.splitext(os.path.basename(audio_path))[0]
            midi_path = os.path.join(midi_dir, f"{base_name}.mid")
            audio_to_midi(audio_path, midi_path)

            # Convert MIDI to Sheet Music
            result = convert_audio_sheet(midi_path, user_skill, model_path="myproject/improved_model.pth)

            # Save paths in model
            music_request.midi_file.name = os.path.relpath(result["midi"], settings.MEDIA_ROOT)
            music_request.sheet_music.name = os.path.relpath(result["xml"], settings.MEDIA_ROOT)
            music_request.status = 'completed'
            music_request.save()

            return redirect('result', pk=music_request.pk)

    else:
        form = MusicRequestForm()

    return render(request, 'main/upload.html', {'form': form})


def result_view(request, pk):
    music_request = get_object_or_404(MusicRequest, pk=pk)
    return render(request, 'main/result.html', {'music_request': music_request})
