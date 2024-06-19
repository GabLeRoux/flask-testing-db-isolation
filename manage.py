import unittest

from flask.cli import FlaskGroup

from app import create_app

app = create_app("testing")  # Utilisez l'environnement de test
cli = FlaskGroup(app)


@cli.command("test")
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    cli()
