% Define the ODE function
f = @(t, y) (1-y)./(1.95-y) - y./(0.05+y);

% Initial conditions (vector format)
y0 = [0; 1; 2];

% Time range
t = linspace(1, 10);

% Solve the ODE numerically using ode45
[t, y] = ode45(f, t, y0);

% Plot the solution
plot(t, y);
xlabel('Time');
ylabel('y');
