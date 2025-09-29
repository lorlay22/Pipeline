import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def simulate_machine_data(machine_id: int, date: str, output_path: str):
    """
    Simulates one day of sensor data for a single industrial machine and saves it to a CSV file.
    Introduces some missing values and outliers to make the cleaning step meaningful.
    """
    print(f"Simulating data for machine {machine_id} on {date}...")
    
    start_time = datetime.strptime(date, "%Y-%m-%d")
    timestamps = [start_time + timedelta(minutes=i*5) for i in range(288)] # 24h * 12 (5-min intervals)
    
    data = {
        "timestamp": timestamps,
        "machine_id": f"machine_{machine_id:02}",
        "temperature": np.random.normal(loc=85.0, scale=5.0, size=288),
        "pressure": np.random.normal(loc=120.0, scale=10.0, size=288),
        "vibration": np.random.normal(loc=0.5, scale=0.1, size=288),
        "status_code": np.random.choice([101, 102, 201, 503], size=288, p=[0.94, 0.02, 0.03, 0.01])
    }
    
    df = pd.DataFrame(data)

    # Introduce some data quality issues to be cleaned later
    df.loc[df.sample(frac=0.05).index, 'temperature'] = np.nan
    df.loc[df.sample(frac=0.02).index, 'pressure'] *= 1.5

    os.makedirs(output_path, exist_ok=True)
    
    file_name = f"machine_{machine_id:02}_{date}.csv"
    df.to_csv(os.path.join(output_path, file_name), index=False)
    print(f"  -> Saved to {os.path.join(output_path, file_name)}")
