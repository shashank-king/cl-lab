import sounddevice as sd
from scipy.io import wavfile

# Read the WAV file
sample_rate, audio_data = wavfile.read('/home/rguktrkvalley/AllClLabPrograms/Classical.wav')

# Reverse the audio data
reversed_audio = audio_data[::-1]

# Play the reversed audio
sd.play(reversed_audio, samplerate=sample_rate)

