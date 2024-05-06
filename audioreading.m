# Read the WAV file
[y, fs] = audioread('/home/rguktrkvalley/AllClLabPrograms/Chorus.wav');

# Plot the audio data (time series)
plot(y);
xlabel('Time (samples)');
ylabel('Amplitude');
title('WAV File Audio Data');
