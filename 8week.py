import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file names
directory = ""  # Change this if needed
files = {
    "X": "iPhone Thing-Accelerometer_X.csv",
    "Y": "iPhone Thing-Accelerometer_Y.csv",
    "Z": "iPhone Thing-Accelerometer_Z.csv"
}

# Read the CSV files
df_x = pd.read_csv(os.path.join(directory, files["X"]), names=['time', 'x'])
df_y = pd.read_csv(os.path.join(directory, files["Y"]), names=['time', 'y'])
df_z = pd.read_csv(os.path.join(directory, files["Z"]), names=['time', 'z'])

# Convert time to datetime format (assuming time is the first column)
df_x['time'] = pd.to_datetime(df_x['time'], errors='coerce')
df_y['time'] = pd.to_datetime(df_y['time'], errors='coerce')
df_z['time'] = pd.to_datetime(df_z['time'], errors='coerce')

# Plot individual graphs
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(df_x['time'], df_x['x'], label="Accelerometer X", color='r')
plt.xlabel("Time")
plt.ylabel("X-axis")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df_y['time'], df_y['y'], label="Accelerometer Y", color='g')
plt.xlabel("Time")
plt.ylabel("Y-axis")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(df_z['time'], df_z['z'], label="Accelerometer Z", color='b')
plt.xlabel("Time")
plt.ylabel("Z-axis")
plt.legend()

plt.tight_layout()
plt.show()

# Combined graph
plt.figure(figsize=(10, 5))
plt.plot(df_x['time'], df_x['x'], label="X-axis", color='r')
plt.plot(df_y['time'], df_y['y'], label="Y-axis", color='g')
plt.plot(df_z['time'], df_z['z'], label="Z-axis", color='b')

plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.legend()
plt.title("Accelerometer Data (X, Y, Z)")
plt.show()
