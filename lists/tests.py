from django.test import TestCase
from lists.views import homepage
from django.urls import resolve

# Create your tests here.

class HomePageTest(TestCase):
    def test_url(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    # testing for homepage and it should correct html 
    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # testing post request and saving them
    def test_post_request(self):
        response = self.client.post('/', data={'item': 'A new list item'}) 
        self.assertIn('A new list item', response.content.decode())

    
    
   