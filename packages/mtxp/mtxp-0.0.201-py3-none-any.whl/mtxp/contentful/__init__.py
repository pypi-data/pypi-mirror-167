
from flask import Blueprint
contentful_blue = Blueprint('contentful', __name__, url_prefix='/contentful')
from mtxp.contentful import views
