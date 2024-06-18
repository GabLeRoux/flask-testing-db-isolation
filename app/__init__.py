from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')
    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app
