import numpy as np
import pretty_midi
from music21 import converter

def midi_to_pianoroll(midi_file, fs=16):
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    n_steps = int(midi_data.get_end_time() * fs) + 1
    roll = np.zeros((n_steps, 88), dtype=np.float32)
    for inst in midi_data.instruments:
        for n in inst.notes:
            idx = n.pitch - 21
            if 0 <= idx < 88:
                roll[int(n.start*fs):int(n.end*fs), idx] = n.velocity / 127.0
    return roll

def pianoroll_to_midi(roll, output_file, fs=16):
    midi_data = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)
    n_steps, n_notes = roll.shape
    for pitch_idx in range(n_notes):
        note_active = False
        for t in range(n_steps):
            vel = int(roll[t, pitch_idx] * 127)
            if vel > 0 and not note_active:
                note_active, start = True, t / fs
            elif (vel == 0 or t == n_steps-1) and note_active:
                note_active = False
                end = t / fs
                piano.notes.append(pretty_midi.Note(
                    velocity=max(vel, 60),
                    pitch=pitch_idx+21,
                    start=start,
                    end=end))
    midi_data.instruments.append(piano)
    midi_data.write(output_file)

def note_density(roll):
    return np.mean(np.sum(roll > 0, axis=1))

def key_complexity(midi_file):
    k = converter.parse(midi_file).analyze('key')
    return 0 if k.mode == 'major' else 1

def pitch_complexity(roll):
    return int(np.ptp(np.where(roll > 0)[1]) > 12)

def overallComplexity(midi_file, roll):
    score = note_density(roll) + key_complexity(midi_file) + pitch_complexity(roll)
    return "hard" if score >= 3 else "easy"

def add_difficulty_channel(roll, target_diff):
    c = np.ones((roll.shape[0], 1), np.float32)
    if target_diff == 'easy':
        c[:] = 0
    elif target_diff == 'hard':
        c[:] = 1
    return np.concatenate([roll, c], axis=1)
