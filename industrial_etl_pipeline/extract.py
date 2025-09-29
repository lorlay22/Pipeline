import os
import pandas as pd

def extract_data(source_dir: str) -> pd.DataFrame:
    """
    Extracts all CSV data from a source directory and combines them into a single DataFrame.
    """
    all_files = [os.path.join(source_dir, f) for f in os.listdir(source_dir) if f.endswith('.csv')]
    
    if not all_files:
        print("No CSV files found in the source directory.")
        return pd.DataFrame()

    print(f"Found {len(all_files)} files to extract.")
    
    df_list = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    
    print(f"Successfully extracted and combined {len(combined_df)} rows.")
    return combined_df
