import unittest
from ner_client import NamedEntityClient

class TestNERClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_input(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    