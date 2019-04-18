from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()

    def test_homepage(self):
        self.browser.get('http://localhost:8000')

        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)
        self.fail('finish this test')

if __name__ == "__main__":
    unittest.main()



