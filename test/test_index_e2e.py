import unittest
from selenium import webdriver

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'/OneDrive/Documents/codeproject_tools/gekodriver')
        self.driver.get('http://localhost:5000') # could be deployed to a staging environment
    
    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)