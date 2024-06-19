import logging

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    logging.basicConfig(level=logging.DEBUG)
    app = Flask(__name__)
    app.config.from_object(f"app.config.{config_name.capitalize()}Config")
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes
        routes.init_app(app)
        logging.debug("Routes and models imported and database created")
        logging.debug(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        logging.debug(f"Testing Mode: {app.config['TESTING']}")

        for rule in app.url_map.iter_rules():
            logging.debug(f"Rule: {rule}, Endpoint: {rule.endpoint}")

    return app
