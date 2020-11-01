from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import models
