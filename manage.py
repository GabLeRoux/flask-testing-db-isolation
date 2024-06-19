import os
import unittest

from flask.cli import FlaskGroup
from flask_migrate import upgrade
from sqlalchemy_utils import database_exists, create_database

from app import create_app, db

env = os.getenv('FLASK_ENV', 'default')
app = create_app(env)
cli = FlaskGroup(app)


@cli.command('test')
def test():
    """Runs the unit tests."""
    app = create_app('testing')
    with app.app_context():
        # Crée la base de données de test si elle n'existe pas
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        # Applique les migrations à la base de données de test
        upgrade()
        tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
            return 0
        return 1


if __name__ == '__main__':
    cli()
