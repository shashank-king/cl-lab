function y = f(x)  % Define the function to integrate
  y = x^2 + 3*x + 1;
end

function integral = trapezoidal_rule(f, a, b, n)
  h = (b - a) / n;
  x = linspace(a, b, n + 1);
  y = f(x);
  integral = h * (0.5 * y(1) + sum(y(2:end-1)) + 0.5 * y(end));
end

% Define integration limits and number of trapezoids
a = 0;
b = 4;
n = 100;

% Calculate the numerical integral using the trapezoidal rule
integral = trapezoidal_rule(f, a, b, n);

% Define x-values for plotting the function
x_plot = linspace(a, b, 1000);

% Plot the function and the estimated integral value
plot(x_plot, f(x_plot), 'b', 'label', 'Original function');
hold on;
plot([a b], [integral integral], 'r--', 'label', 'Numerical integral');
hold off;
xlabel('x');
ylabel('y');
legend;
title('Plot of Original Function and Numerical Integral');
