import os
import glob
import pandas as pd

# Output file
output_file = "latency_folder_results.txt"

def read_until_empty(file_path):
    """Read only the first column of a CSV file until the first empty line."""
    values = []
    with open(file_path, "r") as f:
        for line in f:
            if line.strip() == "":  # stop if empty line
                break
            parts = line.strip().split(",")
            if parts and parts[0]:  # only take first column
                values.append(float(parts[0]))
    return pd.Series(values)

with open(output_file, "w") as f_out:
    for csv_file in glob.glob("*.csv"):  # current folder
        print(f"Processing {csv_file}...")
        values = read_until_empty(csv_file)

        if values.empty:
            continue

        min_val = values.min()
        max_val = values.max()
        avg_val = values.mean()
        std_dev = values.std()
        jitter = max_val - min_val

        f_out.write(f"Results for {csv_file}\n")
        f_out.write(f"  Min: {min_val:.3f}\n")
        f_out.write(f"  Max: {max_val:.3f}\n")
        f_out.write(f"  Avg: {avg_val:.3f}\n")
        f_out.write(f"  Std Deviation: {std_dev:.3f}\n")
        f_out.write(f"  Jitter: {jitter:.3f}\n\n")

print(f"Results saved to {output_file}")
