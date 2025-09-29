import pandas as pd
from google.cloud import bigquery
import json

def create_bq_table_if_not_exists(project_id: str, dataset_id: str, table_id: str, schema_path: str):
    """Checks if a BigQuery table exists, and creates it if it doesn't."""
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    try:
        client.get_table(table_ref)
        print(f"Table {project_id}.{dataset_id}.{table_id} already exists.")
    except Exception:
        print(f"Table {project_id}.{dataset_id}.{table_id} not found. Creating it...")
        try:
            client.get_dataset(dataset_ref)
        except Exception:
            print(f"Dataset {dataset_id} not found. Creating it...")
            client.create_dataset(dataset_ref)
            
        with open(schema_path, 'r') as f:
            schema_json = json.load(f)
        
        schema = [bigquery.SchemaField(field['name'], field['type']) for field in schema_json]
        
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        print("Table created successfully.")


def load_to_bigquery(df: pd.DataFrame, project_id: str, dataset_id: str, table_id: str, schema_path: str):
    """
    Loads a Pandas DataFrame into a BigQuery table.
    """
    if df.empty:
        print("DataFrame is empty. Nothing to load.")
        return

    # Ensure table exists before loading
    create_bq_table_if_not_exists(project_id, dataset_id, table_id, schema_path)

    destination_table = f"{dataset_id}.{table_id}"
    
    print(f"Loading {len(df)} rows to BigQuery table {destination_table}...")
    
    try:
        df.to_gbq(
            destination_table=destination_table,
            project_id=project_id,
            if_exists='append',
            chunksize=10000, # Load in chunks
            progress_bar=True
        )
        print("Successfully loaded data to BigQuery.")
    except Exception as e:
        print(f"An error occurred while loading data to BigQuery: {e}")
