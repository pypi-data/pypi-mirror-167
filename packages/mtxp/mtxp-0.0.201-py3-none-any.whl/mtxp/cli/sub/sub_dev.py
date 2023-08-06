#!/usr/bin/env python3
import os
import sys
import subprocess
import shlex
from dotenv import load_dotenv, find_dotenv
import logging
import argparse
from mtxp.app import app
# from ..services.services import start_all_services
from mtlibs.docker_helper import isInContainer
# logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)

# load_dotenv(".env")

def command(args):
    logger.info(f"app: {app}")
    # from ..services.services import start_all_services
    # if not is_running_from_reloader():
    #     if isInContainer():
    #         start_all_services()
    app.run(debug=True, host='0.0.0.0', port=5000)
