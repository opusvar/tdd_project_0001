import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Steve Malkmus is in a good band."})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_results_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Kamala Harris" })
            assert response._status_code == 200
            data = json.loads(response.get_data())
            assert len(data['entities'] > 0)
