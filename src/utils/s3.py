# -*- coding: utf-8 -*-
"""
VNC Recall
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import boto3, os

load_dotenv(find_dotenv())

s3_client = boto3.client(
    's3',
    endpoint_url=os.getenv('S3_ENDPOINT'),
    region_name=os.getenv('S3_REGION'),
    aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
)

bucket_name = os.getenv('S3_BUCKET')

def save_screenshot(tmp_file_path: Path, s3_file_key: str):
    """ Save a screenshot to a S3 bucket.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Args:
            tmp_file_path (Path): The path to the screenshot file.
            s3_file_key (str): The key to use in the S3 bucket.
    """
    s3_client.upload_file(
        Filename=tmp_file_path.absolute(),
        Bucket=bucket_name,
        Key=s3_file_key,
    )

    print(f'Screenshot saved to s3://{bucket_name}/{s3_file_key}')
