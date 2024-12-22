# -*- coding: utf-8 -*-
"""
VNC Recall
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from vncdotool.client import VNCDoToolClient
from dotenv import load_dotenv, find_dotenv
from vncdotool import api
from pathlib import Path
from uuid import uuid4
import os

load_dotenv(find_dotenv())

def take_screenshot() -> Path:
    """ Take a screenshot of the VNC server and save it to a temporary file.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Returns:
            (Path) The path to the temporary file.
    """
    client: VNCDoToolClient # Just for type hinting
    with api.connect(
            server=os.getenv('VNC_SERVER'),
            password=os.getenv('VNC_PASSWORD'),
            timeout=int(os.getenv('TIMEOUT', 10)),
    ) as client:
        # Save the screenshot to a unique temporary file
        tmp_file_path = Path(f'tmp/screenshot_{str(uuid4())}.png')

        client.captureScreen(tmp_file_path.absolute())
        client.disconnect()

    print(f'Screenshot saved temporarily to {tmp_file_path}')
    return tmp_file_path
