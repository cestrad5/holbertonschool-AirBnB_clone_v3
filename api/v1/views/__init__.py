#!/usr/bin/python3
"""Package that manage all the routes"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1') # Adding a url prefix

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *