import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load and prepare data
data = pd.read_csv('sample_week7.csv')
data = data.rename(columns={'Temperature (°C)': 'Temperature', 'Humidity (%)': 'Humidity'})
X = data['Temperature'].values.reshape(-1, 1)
y = data['Humidity'].values

# Create and fit initial model
model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)

# Calculate residuals and identify outliers
residuals = np.abs(y - pred)
outlier_threshold = np.percentile(residuals, 95)
outliers = residuals > outlier_threshold
filtered_data = data[~outliers]
X_filtered = filtered_data['Temperature'].values.reshape(-1, 1)
y_filtered = filtered_data['Humidity'].values

# GRAPH 1: Simple Linear Regression
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', alpha=0.5, label='Data Points')
plt.plot(X, pred, color='red', linewidth=2, 
         label=f'Regression Line (R²={r2_score(y, pred):.2f})')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('1. Simple Linear Regression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# GRAPH 2: Outliers Highlighted
plt.figure(figsize=(8, 6))
plt.scatter(X[~outliers], y[~outliers], color='blue', alpha=0.5, label='Normal Data')
plt.scatter(X[outliers], y[outliers], color='orange', alpha=0.8, 
            label=f'Outliers (top {100-95}%)')
plt.plot(X, pred, color='red', linewidth=2, label='Original Regression')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('2. Outliers Identification')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# GRAPH 3: Filtered Data Regression
model_filtered = LinearRegression()
model_filtered.fit(X_filtered, y_filtered)
pred_filtered = model_filtered.predict(X_filtered)

plt.figure(figsize=(8, 6))
plt.scatter(X_filtered, y_filtered, color='green', alpha=0.5, label='Filtered Data')
plt.plot(X_filtered, pred_filtered, color='purple', linewidth=2,
         label=f'Filtered Regression (R²={r2_score(y_filtered, pred_filtered):.2f})')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('3. Filtered Data Regression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print comparison of models
print("\nModel Comparison:")
print(f"Original R-squared: {r2_score(y, pred):.4f}")
print(f"Filtered R-squared: {r2_score(y_filtered, pred_filtered):.4f}")
print(f"Number of outliers removed: {len(data) - len(filtered_data)}")