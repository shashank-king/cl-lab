import matplotlib.pyplot as plt
import wave
import numpy as np
with wave.open('/home/rguktrkvalley/AllClLabPrograms/Chorus.wav', 'rb') as wav_file:
    audio_data = wav_file.readframes(wav_file.getnframes())
audio_array = np.frombuffer(audio_data, dtype=np.int16)
plt.plot(audio_array)
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.title('WAV File Audio Data')
plt.show()

