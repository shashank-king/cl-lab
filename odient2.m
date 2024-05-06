% Define the ODE function
f = @(t, y) -y.*t + 13;

% Initial condition
y0 = 1;

% Time range
t = linspace(0, 5);

% Solve the ODE numerically using ode45
[t, y] = ode45(f, t, y0);

% Plot the solution
plot(t, y);
xlabel('Time');
ylabel('y');
