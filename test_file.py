from flask_testing import TestCase
from counter import app, read_counter, update_counter

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_request(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn("Current POST requests count:", response.data.decode())

    def test_post_request(self):
        initial_count = read_counter()
        response = self.client.post('/')
        self.assert200(response)
        updated_count = read_counter()
        self.assertEqual(updated_count, initial_count + 1)
        self.assertIn(f"POST requests counter updated. Current count: {updated_count}", response.data.decode())