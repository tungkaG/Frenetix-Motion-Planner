import csv
import matplotlib.pyplot as plt
import numpy as np
import os

# Path to your log file
log_file_path = 'important_logs/latency_log_vehicle_20250904_113434.csv'

# Lists to store latencies
planning_latencies = []
sampling_latencies = []

# Load data from CSV
with open(log_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) != 2:
            # Skip malformed rows (like the CPU stats line at the end)
            print(f"⚠️ Skipping invalid row: {row}")
            continue
        try:
            planning, sampling = float(row[0]), float(row[1])
            planning_latencies.append(planning)
            sampling_latencies.append(sampling)
        except ValueError:
            # Handle any row where conversion to float fails
            print(f"⚠️ Skipping non-numeric row: {row}")
            continue

# Convert to numpy arrays for convenience
planning_latencies = np.array(planning_latencies)
sampling_latencies = np.array(sampling_latencies)

# Calculate stats
def compute_stats(data):
    return {
        'min': np.min(data),
        'max': np.max(data),
        'mean': np.mean(data),
        'std_dev': np.std(data),
        'jitter': np.max(np.abs(np.diff(data)))  # max latency delta between consecutive points
    }

planning_stats = compute_stats(planning_latencies)
sampling_stats = compute_stats(sampling_latencies)

# Print results
print("📊 Planning Latency Stats (ms):")
for k, v in planning_stats.items():
    print(f"  {k}: {v:.2f}")

print("\n📊 Sampling Latency Stats (ms):")
for k, v in sampling_stats.items():
    print(f"  {k}: {v:.2f}")


# ----------- PLOTTING -----------

# 📦 1. Planning Latency
plt.figure(figsize=(10, 5))
plt.suptitle("📊 Planning Latency", fontsize=14)

# Box plot for Planning
plt.subplot(2, 1, 1)
plt.boxplot(planning_latencies)
plt.title("Planning Latency - Box Plot")
plt.ylabel("Latency (ms)")

# Line plot for Planning
plt.subplot(2, 1, 2)
plt.plot(planning_latencies, color='blue')
plt.title("Planning Latency Over Time")
plt.xlabel("Message Index")
plt.ylabel("Latency (ms)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# 📦 2. Sampling Latency
plt.figure(figsize=(10, 5))
plt.suptitle("📊 Sampling Latency", fontsize=14)

# Box plot for Sampling
plt.subplot(2, 1, 1)
plt.boxplot(sampling_latencies)
plt.title("Sampling Latency - Box Plot")
plt.ylabel("Latency (ms)")

# Line plot for Sampling
plt.subplot(2, 1, 2)
plt.plot(sampling_latencies, color='orange')
plt.title("Sampling Latency Over Time")
plt.xlabel("Message Index")
plt.ylabel("Latency (ms)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()