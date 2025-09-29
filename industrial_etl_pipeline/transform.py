import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms the raw machine data.
    """
    if df.empty:
        return df

    print("Starting data transformation and cleaning...")
    
    # 1. Correct Data Types
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # 2. Handle Missing Values
    # For temperature, we'll fill with the median value of that specific machine
    df['temperature'] = df.groupby('machine_id')['temperature'].transform(lambda x: x.fillna(x.median()))
    
    # Drop any other rows that might have NaNs (for simplicity)
    df.dropna(inplace=True)

    # 3. Map Status Codes to Labels (Enrichment)
    status_map = {
        101: 'OPERATIONAL',
        102: 'IDLE',
        201: 'MAINTENANCE',
        503: 'ERROR'
    }
    df['status_label'] = df['status_code'].map(status_map)

    # 4. Outlier Handling (Simple clipping for pressure)
    # This is a simple example; more complex methods exist.
    pressure_upper_bound = df['pressure'].quantile(0.99)
    df['pressure'] = df['pressure'].clip(upper=pressure_upper_bound)
    
    print(f"Transformation complete. Data shape is now: {df.shape}")
    return df
