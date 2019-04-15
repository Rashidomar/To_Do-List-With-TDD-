from django.test import TestCase
from lists.views import homepage
from django.urls import resolve
#from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):
    def test_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)
    
   