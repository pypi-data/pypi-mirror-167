#!/usr/bin/env python3
import os
import sys
import subprocess
import shlex
from dotenv import load_dotenv, find_dotenv
import logging
import argparse
from mtxp.app import app
from mtxp.services.services import start_all_services
from mtlibs.docker_helper import isInContainer
from werkzeug.serving import is_running_from_reloader
logger = logging.getLogger(__name__)


def command(args):
    logger.info(f"默认入口, {args}")
    if not is_running_from_reloader():
        if isInContainer():
            start_all_services()

    app.run(debug=True, host='0.0.0.0', port=5000)
