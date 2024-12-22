# -*- coding: utf-8 -*-
"""
VNC Recall
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv, find_dotenv
from pymongo.server_api import ServerApi
from datetime import datetime
import os

load_dotenv(find_dotenv())

mongo_client = MongoClient(
    os.getenv('MONGO_URI'),
    server_api=ServerApi('1'),
)
screenshot_collection = mongo_client['vnc-recall']['screenshots']

def log_screenshot(s3_file_key: str):
    """ Log a screenshot to a MongoDB collection.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Args:
            s3_file_key (str): The key of the screenshot in the S3 bucket.
    """
    screenshot_collection.insert_one({
        'timestamp': datetime.now(),
        's3_file_key': s3_file_key,
    })

    print(f'Screenshot logged to mongodb://vnc-recall/screenshots')
