from os import getenv
from flask import Flask
from flask_cors import CORS
from app.configs import database, migrations
from app import views

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_KEYS_SORT'] = False

    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)

    return app