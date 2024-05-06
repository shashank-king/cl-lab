# Sample data
x1 = [1, 2, 3];
y1 = [2, 4, 5];
x2 = [4, 5, 6];
y2 = [6, 8, 10];

# Create figure and subplots
figure;
subplot(2, 1, 1);

# Plot data in subplots
plot(x1, y1);
title("Subplot 1");
xlabel("X-axis");
ylabel("Y-axis");

subplot(2, 1, 2);
plot(x2, y2);
title("Subplot 2");
xlabel("X-axis");
ylabel("Y-axis");

# Adjust spacing and layout
grid on;
