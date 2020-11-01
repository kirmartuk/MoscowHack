from flask import Blueprint

bp = Blueprint('api', __name__)


from app.api import shelters, documents, dicts, animals, history, requests
