# test_app.py
import unittest
from main import app, guestbook

class GuestbookTestCase(unittest.TestCase):

    # Ensure the home page loads correctly
    def test_homepage_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Guestbook', response.data)

    # Ensure submitting a name adds it to the guestbook
    def test_add_name(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(name='John Doe'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)

        # Check that the guestbook contains the name
        self.assertIn('John Doe', guestbook)

if __name__ == '__main__':
    unittest.main()
