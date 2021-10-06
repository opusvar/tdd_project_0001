import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get("http://localhost:5000")
        # self.driver = webdriver.Firefox(executable_path=r'/onedrive/documents/codeproject_tools/gekodriver.exe')
        # self.driver.get('http://localhost:5000') # could be deployed to a staging environment
    
    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)