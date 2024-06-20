from flask import Flask

from app.blueprints.commands import commands
from app.blueprints.main import main
from app.config import Config
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(commands)
    app.register_blueprint(main)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
