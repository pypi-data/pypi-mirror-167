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
logger = logging.getLogger(__name__)

# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)

# load_dotenv(".env")

def command(args):
    """启动后台相关服务"""
    logger.info(f"启动后台服务")
    start_all_services()
