import matplotlib.pyplot as plt

# Sample data
x1 = [1, 2, 3]
y1 = [2, 4, 5]
x2 = [4, 5, 6]
y2 = [6, 8, 10]

# Create figure and subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Plot data in subplots
axes[0].plot(x1, y1, label="Data 1")
axes[1].plot(x2, y2, label="Data 2")

# Add labels and titles
fig.suptitle("Subplots Example")
axes[0].set_title("Subplot 1")
axes[1].set_title("Subplot 2")

# Add legends
axes[0].legend()
axes[1].legend()

# Adjust spacing and layout
plt.tight_layout()

# Display the plot
plt.show()

