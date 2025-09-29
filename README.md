# Industrial IoT ETL Pipeline for Process Control

This repository demonstrates a complete, automated ETL (Extract, Transform, Load) pipeline written in Python. It simulates daily data collection from multiple industrial machines, processes and cleans the data, and loads it into Google BigQuery for analysis.

This project is a practical implementation of the skills and experience listed on my resume, specifically concerning the design of automated data flows and process control monitoring.

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
2.  **Transform**: The raw data is loaded into a Pandas DataFrame. It undergoes a cleaning process which includes:
    - Handling missing values (e.g., filling with median temperature).
    - Correcting data types (e.g., converting timestamps).
    - Mapping status codes to human-readable labels (e.g., 101 -> 'OPERATIONAL').
    - Creating new, valuable features (e.g., calculating machine operating hours).
3.  **Load**: The clean, transformed data is appended to a table in Google BigQuery, ready for analysis and dashboarding (e.g., in Looker Studio).

## How to Run This Project

### 1. Prerequisites
- Python 3.7+
- A Google Cloud Platform (GCP) project with BigQuery API enabled.
- `gcloud` CLI installed and authenticated.

### 2. Setup
Clone the repository:
```bash
git clone [https://github.com/VOTRE_NOM_UTILISATEUR/industrial-etl-pipeline.git](https://github.com/VOTRE_NOM_UTILISATEUR/industrial-etl-pipeline.git)
cd industrial-etl-pipeline
