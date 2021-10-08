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

    def test_page_heading_is_named_enity_finder(self):
        heading = self._find("heading").text
        self.assertEqual('Named Entity Finder', heading)

    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f"[data-test-id='{val}']")