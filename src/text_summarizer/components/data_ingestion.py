import os
from pathlib import Path
import boto3
from dotenv import load_dotenv
import zipfile
from io import BytesIO
import requests

from text_summarizer.logging import logger


class DataIngestion:
    def __init__(self, config):
        self.root_dir = config["root_dir"]
        self.data_class_path = config["data_class_path"]
        self.bucket = config["AWS_BUCKET_NAME"]
        self.key = config["AWS_DATASET_NAME"]

    def download_files_from_HuggingFace(self):
        """
        Downloads the files from HuggingFace to the data directory

        """        

        url = "https://huggingface.co/datasets/samsum/raw/main/samsum.py"
        response = requests.get(url)

        with open(self.data_class_path, "wb") as f:
            f.write(response.content)


    def download_files_from_cloud(self):
        """
        Downloads the files from AWS s3 to the data directory

        """        
        # Load environmental variables from .env file
        dotenv_path = os.path.join('config', '.env')
        load_dotenv(dotenv_path)

        AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
        AWS_REGION=os.environ.get("AWS_REGION")

        # Create an S3 client
        s3 = boto3.client(service_name='s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        # Read the zip file from S3
        response = s3.get_object(Bucket=self.bucket, Key=self.key)
        datasetZip = response['Body'].read()

        # Extract all contents to a specified directory
        self.extract_csv_files(datasetZip)

        logger.info(f"Download successful!")

    def extract_csv_files(self, datasetZip):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        # Create a BytesIO object from the zip file content
        zip_buffer = BytesIO(datasetZip)

        with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
            # Get the list of files in the ZIP archive
            file_list = zip_ref.namelist()
            for file_name in file_list:
                if file_name.endswith('.csv'):
                    zip_ref.extract(file_name, self.root_dir)
        