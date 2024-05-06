import scipy.io.wavfile as wav
filename = "audio.wav"
sample_rate, data = wav.read(filename)
data = data.astype(float)
