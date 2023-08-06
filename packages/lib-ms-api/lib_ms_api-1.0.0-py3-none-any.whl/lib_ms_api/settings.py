from flask import Flask
from flask_cli import FlaskCLI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(database_uri: str, track: bool, debug: bool):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = track
    app.config['DEBUG'] = debug

    db = SQLAlchemy(app)
    Migrate(app, db)
    FlaskCLI(app)

    return app, db
