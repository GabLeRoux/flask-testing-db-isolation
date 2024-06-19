import unittest

from sqlalchemy import inspect

from app import create_app, db
from app.models import User


class UserRoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        inspector = inspect(db.engine)
        print("Database tables: ", inspector.get_table_names())

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_and_get_user_1(self):
        user = User(username="testuser1")
        db.session.add(user)
        db.session.commit()

        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0], "testuser1")

    def test_create_and_get_user_2(self):
        user = User(username="testuser2")
        db.session.add(user)
        db.session.commit()

        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0], "testuser2")

    def test_routes_exist(self):
        response = self.client.get("/users")
        self.assertNotEqual(response.status_code, 404, "Route /users does not exist")

    def test_manual_route_check(self):
        response = self.client.get("/users")
        print(f"Manual Route Check: Status Code {response.status_code}")
        print(f"Manual Route Check: Response {response.data}")


if __name__ == "__main__":
    unittest.main()
