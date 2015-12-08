from django.test import TestCase, Client


class LoginPageTestCase(TestCase):
    def authentication_test(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        response = c.post('/login/', {'name': 'alexf', 'password': '12345'})
        self.assertEqual(200, response.status_code)

    def test_login_required(self):
        response = self.client.get('/teachers', follow=True)
        self.assertIn('<button type="submit" class="btn btn-default">Login</button>', response.content)


class ButtonAvailabilityTests(TestCase):
    def login_button_availability(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        response = c.get('/login/')
        self.assertIn('<button type="submit" class="btn btn-default">Login</button>', response.content)

    def logout_button_availability(self):
        self.client.login(username='alexf', password='1234')
        response = self.client.get('/')
        self.assertTrue('<a href="/logout/?next=/">Logout</a>', response.content)
