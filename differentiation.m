function y = f(x)  % Define the function to differentiate
  y = x^2 + 3*x + 1;
end

function dy_dx = central_difference(f, x, h)

  dy_dx = (f(x + h) - f(x - h)) / (2 * h);
end

% Define the range of x-values
x = linspace(-2, 4, 100);

% Calculate numerical derivatives using central difference
dy_dx = central_difference(f, x, 0.01);

% Plot the original function and its numerical derivative
plot(x, f(x), 'b', 'label', 'Original function');
hold on;
plot(x, dy_dx, 'r', 'label', 'Numerical derivative (central difference)');
hold off;
xlabel('x');
ylabel('y');
legend;
title('Plot of Original Function and Numerical Derivative');

