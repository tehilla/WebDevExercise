from tornado.testing import AsyncHTTPTestCase
from tornado.escape import json_decode
from app import make_app
import unittest
import json


class HandlerBaseTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def fetch_json(self, *args, **kwargs):
        response = self.fetch(*args, **kwargs)
        response.rethrow()
        return json_decode(response.body)


class MainHandlerTestCase(HandlerBaseTestCase):
    def fetch_calculate_post(self, input_data, calculator_state):
        response = self.fetch("/calculate", method="POST",
                              body=json.dumps({"input": input_data, "calculatorState": calculator_state}))
        response.rethrow()
        return json_decode(response.body)

    def test_calculate_empty_json(self):
        response = self.fetch("/calculate", method="POST",
                              body=json.dumps({}))
        response.rethrow()
        json_data = json_decode(response.body)
        self.assertEqual('Invalid input', json_data["display"])

    def test_empty_input(self):
        json_data = self.fetch_calculate_post(None, None)
        self.assertEqual('Invalid input', json_data["display"])

    def test_empty_state_input_number(self):
        json_data = self.fetch_calculate_post('1', None)
        self.assertEqual('1', json_data["display"])

    def test_empty_state_input_operation(self):
        json_data = self.fetch_calculate_post('+', None)
        self.assertEqual('Invalid input', json_data["display"])

    def test_exercise_example(self):
        json_data = self.fetch_calculate_post('1', None)
        self.assertEqual('1', json_data["display"])
        json_data = self.fetch_calculate_post('2', json_data)
        self.assertEqual('12', json_data["display"])
        json_data = self.fetch_calculate_post('+', json_data)
        self.assertEqual('12', json_data["display"])
        json_data = self.fetch_calculate_post('4', json_data)
        self.assertEqual('4', json_data["display"])
        json_data = self.fetch_calculate_post('3', json_data)
        self.assertEqual('43', json_data["display"])
        json_data = self.fetch_calculate_post('=', json_data)
        self.assertEqual('55', json_data["display"])
        json_data = self.fetch_calculate_post('+', json_data)
        self.assertEqual('55', json_data["display"])
        json_data = self.fetch_calculate_post('1', json_data)
        self.assertEqual('1', json_data["display"])
        json_data = self.fetch_calculate_post('=', json_data)
        self.assertEqual('56', json_data["display"])
        json_data = self.fetch_calculate_post('5', json_data)
        self.assertEqual('5', json_data["display"])


if __name__ == "__main__":
    unittest.main()
