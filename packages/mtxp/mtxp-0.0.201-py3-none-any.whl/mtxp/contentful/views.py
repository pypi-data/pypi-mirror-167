from . import contentful_blue
import yaml
import os
import logging
from os.path import join
from pathlib import Path
    
logger = logging.getLogger(__name__)

@contentful_blue.route('/')
def home():
    return 'contentful'
 
@contentful_blue.route('/reset')
def api_reset():
    return 'reset'
 