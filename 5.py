import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv("graph_data.csv")

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
fig.suptitle("Data Over Time")

# Plot X-axis data
axs[0].plot(df["Time"], df["X-axis"], color='blue', label='X-axis')
axs[0].set_ylabel("X-axis (°/s)")
axs[0].legend()
axs[0].grid(True)

# Plot Y-axis data
axs[1].plot(df["Time"], df["Y-axis"], color='green', label='Y-axis')
axs[1].set_ylabel("Y-axis (°/s)")
axs[1].legend()
axs[1].grid(True)

# Plot Z-axis data
axs[2].plot(df["Time"], df["Z-axis"], color='red', label='Z-axis')
axs[2].set_ylabel("Z-axis (°/s)")
axs[2].set_xlabel("Time (s)")
axs[2].legend()
axs[2].grid(True)

# Show the plot
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
