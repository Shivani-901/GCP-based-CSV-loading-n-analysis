import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Replace with your project ID, dataset ID, and GitHub CSV URL
project_id = 'student-analytics-414009'
dataset_id = 'student-analytics-414009'
table_id = 'student'  # Replace with your desired table ID
github_url = 'https://raw.githubusercontent.com/ShapeLab/ZooidsCompositePhysicalizations/master/Zooid_Vis/bin/data/student-dataset.csv'

# Read CSV from GitHub
df = pd.read_csv(github_url)

# Initialize BigQuery client
credentials_path = "C:\\Users\\lenovo\\Downloads\\client_secret_452093773520-fpeecsqhr2ulmv14omks5653h4rladdl.apps.googleusercontent.com (1).json"  # Replace with the path to your service account key JSON file
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# Set the table_id to the table you want to create or overwrite in BigQuery
table_id = f"{project_id}.{dataset_id}.{table_id}"

# Upload DataFrame to BigQuery
df.to_gbq(destination_table=table_id, project_id=project_id, if_exists='replace')
