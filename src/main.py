# -*- coding: utf-8 -*-
"""
VNC Recall
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from dotenv import load_dotenv, find_dotenv
from utils.mongo import log_screenshot
from utils.vnc import take_screenshot
from utils.s3 import save_screenshot
from datetime import datetime
from vncdotool import api
from time import sleep
import os

load_dotenv(find_dotenv())

def main():
    """ Main function of the VNC Recall program.
        Take a screenshot of the VNC server, save it to an S3 bucket, and log it to a MongoDB collection.
        Repeat this process every INTERVAL seconds.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>
    """
    while True:
        try:
            try:
                tmp_file_path = take_screenshot()

                now = datetime.now()
                s3_file_key = f'{now.strftime("%Y-%m-%d")}/{now.strftime("%H-%M-%S")}.png'

                save_screenshot(
                    tmp_file_path=tmp_file_path,
                    s3_file_key=s3_file_key,
                )

                log_screenshot(
                    s3_file_key=s3_file_key,
                )

                tmp_file_path.unlink()
            except:
                pass

            sleep(int(os.getenv('INTERVAL', 60)))
        except KeyboardInterrupt:
            print('Exiting...')
            break

    api.shutdown()

if __name__ == '__main__':
    main()
