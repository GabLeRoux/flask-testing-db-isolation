import unittest
from sqlalchemy import inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from app import create_app, db
from app.models import User
from flask_migrate import upgrade

class UserRoutesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        # Applique les migrations à la base de données de test
        with cls.app_context:
            upgrade()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        self.connection = db.engine.connect()
        self.transaction = self.connection.begin()
        self.session_factory = sessionmaker(bind=self.connection)
        self.Session = scoped_session(self.session_factory)
        db.session = self.Session

    def tearDown(self):
        self.transaction.rollback()
        self.connection.close()
        self.Session.remove()

    def test_create_and_get_user_1(self):
        user = User(username='testuser1')
        db.session.add(user)
        db.session.commit()

        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0], 'testuser1')

    def test_create_and_get_user_2(self):
        user = User(username='testuser2')
        db.session.add(user)
        db.session.commit()

        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0], 'testuser2')

    def test_routes_exist(self):
        response = self.client.get('/users')
        self.assertNotEqual(response.status_code, 404, "Route /users does not exist")

    def test_manual_route_check(self):
        response = self.client.get('/users')
        print(f"Manual Route Check: Status Code {response.status_code}")
        print(f"Manual Route Check: Response {response.data}")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
