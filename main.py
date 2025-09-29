import config
from industrial_etl_pipeline import data_simulator, extract, transform, load
from datetime import datetime, timedelta
import os

def run_pipeline():
    """Main function to orchestrate the ETL pipeline."""
    
    # SIMULATION STEP
    print("Starting Data Simulation Step ")
    yesterday = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
    for i in range(1, 11): # Simulate 10 machines
        data_simulator.simulate_machine_data(
            machine_id=i, 
            date=yesterday, 
            output_path=config.RAW_DATA_DIR
        )
    print("Data Simulation Complete \n")
    
    # ETL PIPELINE
    print("Starting ETL Pipeline ")
    
    try:
        # 1. Extract
        print("Step 1: Extracting data...")
        raw_df = extract.extract_data(config.RAW_DATA_DIR)
        
        # 2. Transform
        print("\nStep 2: Transforming data...")
        transformed_df = transform.transform_data(raw_df)

        # Optional: Save processed data locally for auditing
        if not transformed_df.empty:
            os.makedirs(config.PROCESSED_DATA_DIR, exist_ok=True)
            processed_file_path = os.path.join(config.PROCESSED_DATA_DIR, f"processed_data_{yesterday}.csv")
            transformed_df.to_csv(processed_file_path, index=False)
            print(f"Saved processed data to {processed_file_path}")

        # 3. Load
        print("\nStep 3: Loading data to BigQuery...")
        load.load_to_bigquery(
            df=transformed_df,
            project_id=config.GCP_PROJECT_ID,
            dataset_id=config.BQ_DATASET,
            table_id=config.BQ_TABLE,
            schema_path=config.SCHEMA_PATH
        )
        
        print("\n--- ETL Pipeline Finished Successfully ---")

    except Exception as e:
        print(f"ETL Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
