% Define parameters
t = 0:0.01:10;  % Time range using colon operator
f1 = 2;  % Frequency of first sine wave
f2 = 3;  % Frequency of second sine wave
a1 = 1;  % Amplitude of first sine wave
a2 = 2;  % Amplitude of second sine wave

% Generate sine waves
y1 = a1 * sin(2*pi*f1*t);
y2 = a2 * sin(2*pi*f2*t);

% Add and subtract
y_sum = y1 + y2;
y_diff = y1 - y2;

% Plot
plot(t, y1, 'b', 'label', 'Sine wave 1');
hold on;
plot(t, y2, 'r', 'label', 'Sine wave 2');
plot(t, y_sum, 'g', 'label', 'Sum');
plot(t, y_diff, 'm', 'label', 'Difference');
legend;
xlabel('Time (t)');
ylabel('Amplitude');
title('Addition and Subtraction of Sine Waves');
