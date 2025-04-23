import pandas as pd
import matplotlib.pyplot as plt
import os

# === Load and clean the CSV file ===
csv_filename = "dht_data.csv"
df = pd.read_csv(csv_filename)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Drop rows with NaN values in any key column
df.dropna(subset=['timestamp', 'temperature', 'humidity'], inplace=True)

# === Plot 1: Temperature ===
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['temperature'], color='red')
plt.title("Temperature Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("temperature_plot.png")
plt.close()

# === Plot 2: Humidity ===
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['humidity'], color='blue')
plt.title("Humidity Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("humidity_plot.png")
plt.close()

# === Plot 3: Combined ===
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['temperature'], color='red', label="Temperature (°C)")
plt.plot(df['timestamp'], df['humidity'], color='blue', label="Humidity (%)")
plt.title("Temperature & Humidity Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Sensor Values")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("combined_plot.png")
plt.close()

# === Confirm Saved Files ===
print(" PNG files generated in current folder:")
for file in ["temperature_plot.png", "humidity_plot.png", "combined_plot.png"]:
    if os.path.exists(file):
        print(" -", file)
    else:
        print(" Not found:", file)
