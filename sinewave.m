% Generate x-values
x_values = 0:0.01:2*pi; % Generating x-values from 0 to 2*pi with a step of 0.01

% Calculate y-values (sine of x)
y_values = sin(x_values);

% Plot the sine wave
plot(x_values, y_values)
title('Sine Wave')
xlabel('x')
ylabel('sin(x)')
grid on
