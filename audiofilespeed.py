import soundfile as sf

# Read the WAV file
audio_data, sample_rate = sf.read('/home/rguktrkvalley/AllClLabPrograms/Chorus.wav')

# Define the desired speed change factor
speed_change_factor = 0.5  # Change to desired factor (e.g., 2 for double speed)

# Resample the audio data
stretched_audio = sf.resample(audio_data, speed_change_factor)

# Play or save the stretched audio
sf.write('stretched_audio.wav', stretched_audio, samplerate=int(sample_rate * speed_change_factor))

