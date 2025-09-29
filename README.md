
# Industrial ETL Pipeline for Process Control

This repository demonstrates a complete, automated ETL (Extract, Transform, Load) pipeline written in Python. It simulates daily data collection from multiple industrial machines, processes and cleans the data, and loads it into Google BigQuery for analysis.

## Project Goal

The primary goal of this pipeline is to automate the daily collection of sensor data from industrial machinery. By centralizing this data in BigQuery, we enable daily monitoring of production quality and efficiency, which in a real-world scenario led to:

  - A **25% reduction in manual analysis time**.
  - Improved reliability of decision-making for continuous production processes.

## Tech Stack

  - **Language:** Python
  - **Data Processing:** Pandas
  - **Cloud Warehouse:** Google BigQuery
  - **Google Cloud Interaction:** `google-cloud-bigquery`, `pandas-gbq`
  - **Automation/Orchestration:** This script is designed to be run by a scheduler like Cron, Airflow, or Google Cloud Scheduler.

## Pipeline Overview

The ETL process is broken down into three main stages:

1.  **Extract**: Raw data files (simulated as CSVs) are collected from a source directory. Each file represents one day of data from one machine.
2.  **Transform**: The raw data is loaded into a Pandas DataFrame. It undergoes a cleaning process which includes handling missing values, correcting data types, and mapping status codes to labels.
3.  **Load**: The clean, transformed data is appended to a table in Google BigQuery, ready for analysis and dashboarding (e.g., in Looker Studio).

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

  - Python 3.7+
  - A Google Cloud Platform (GCP) project with the BigQuery API enabled.
  - Google Cloud SDK (`gcloud` CLI) installed on your machine.

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/VOTRE_NOM_UTILISATEUR/industrial-etl-pipeline.git
    cd industrial-etl-pipeline
    ```

2.  **Install dependencies:**
    Make sure you are in the project directory and run:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Authenticate with Google Cloud:**
    This command allows the script to securely use your credentials to connect to BigQuery.

    ```bash
    gcloud auth application-default login
    ```

4.  **Configure the pipeline:**
    Open the `config.py` file and replace the placeholder with your own GCP Project ID.

    ```python
    # config.py
    GCP_PROJECT_ID = "your-gcp-project-id"
    BQ_DATASET = "industrial_data"
    BQ_TABLE = "machine_process_control"
    ```

    *The script will automatically create the dataset and table if they don't exist.*

### Execute the Pipeline

Once the setup is complete, run the main script from your terminal:

```bash
python main.py
```

This will:

1.  Simulate the creation of 10 raw data files in a `raw_data/` directory.
2.  Run the full ETL pipeline to clean and process these files.
3.  Load the final, clean data into your BigQuery table.

