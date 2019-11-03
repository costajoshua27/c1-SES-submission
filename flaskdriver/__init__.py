from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskdriver.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from flaskdriver.main.routes import main
app.register_blueprint(main)
