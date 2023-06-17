from flask import Blueprint

bp = Blueprint("posts", __name__)

from app.posts import routes


# cia __init__.py cia ir yra blueprint, o prie jo importuojam dar route
