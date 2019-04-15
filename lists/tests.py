from django.test import TestCase
from lists.views import homepage
from django.urls import resolve
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):
    def test_url(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    # testing for homepage and it should correct html 
    def test_homepage(self):
        request = HttpRequest()
        response = homepage(request)
        html = response.content.decode()
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    
    
   