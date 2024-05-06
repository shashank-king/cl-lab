function dydt = returns_dydt(y, t)
  dydt = 13 * exp(t) + y;
endfunction

# Initial condition
y0 = 1;

# Values of time
t = linspace(0, 5);

# Solving ODE using ode45
[t, y] = ode45(returns_dydt, t, y0);

# Plot results
plot(t, y);
xlabel("Time");
ylabel("Y");
