from flask_testing import TestCase
from counter import app, read_counter, update_counter

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_request(self):
        response = self.client.get('/')
        self.assert200(response)
        
        json_data = response.get_json()

    # Assert that the "counter" and "csrf_token" fields exist in the response
        self.assertIn("counter", json_data)
        self.assertIn("csrf_token", json_data)


    def test_post_request(self):
    # Step 1: Get the CSRF token
        response = self.client.get('/')
        self.assert200(response)
        csrf_token = response.json["csrf_token"]

    # Step 2: Use the CSRF token in the POST request
        initial_count = read_counter()
        response = self.client.post('/', headers={'X-CSRFToken': csrf_token})
    
        self.assert200(response)
    
        updated_count = read_counter()
        self.assertEqual(updated_count, initial_count + 1)
        json_data = response.json
        self.assertEqual(json_data["new_counter"], updated_count)
