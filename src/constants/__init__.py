import sys, os
from datetime import datetime

# artifact -> pipeline folder -> timestamp -> output

def get_current_timestamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_timestamp()

# dataset dir
root_dir_key = os.getcwd()
data_dir = 'Waze'
data_dir_key = 'waze_dataset.csv'

# Artifact dir
ARTIFACT_DIR = 'Artifact'

# Data Ingestion related variables
DATA_INGESTION_KEY = 'data_ingestion'
DATA_INGESTION_RAW_DATA_DIR = 'raw_data_dir'
DATA_INGESTION_INGESTED_DATA_DIR = 'ingested_dir'
RAW_DATA_DIR_KEY = 'raw.csv'
TRAIN_DATA_DIR_KEY = 'train.csv'
TEST_DATA_DIR_KEY = 'test.csv'
