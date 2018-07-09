import unittest
import calculator
import json


class CalculatorTests(unittest.TestCase):

    def test_add(self):
        s = '{}'
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "2")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "+")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "4")
        self.assertEqual('4', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "3")
        self.assertEqual('43', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "=")
        self.assertEqual('55', json.loads(s)["display"])

    def test_minus(self):
        s = '{}'
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "2")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "-")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "6")
        self.assertEqual('6', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "=")
        self.assertEqual('6', json.loads(s)["display"])

    def test_multiple(self):
        s = '{}'
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "2")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "*")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "6")
        self.assertEqual('6', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "=")
        self.assertEqual('72', json.loads(s)["display"])

    def test_devide(self):
        s = '{}'
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "2")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "/")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "4")
        self.assertEqual('4', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "=")
        self.assertEqual('3', json.loads(s)["display"])

    def test_neg(self):
        s = '{}'
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "2")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "-")
        self.assertEqual('12', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "4")
        self.assertEqual('4', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "4")
        self.assertEqual('44', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "=")
        self.assertEqual('-32', json.loads(s)["display"])

        s = calculator.calculateNextState(json.dumps({'expression': '12-44', 'end_of_exp': False, 'display': '44'}), "=")
        self.assertEqual('-32', json.loads(s)["display"])

    def test_float(self):
        s = '{}'
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, ".")
        self.assertEqual('1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "1")
        self.assertEqual('1.1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "-")
        self.assertEqual('1.1', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "4")
        self.assertEqual('4', json.loads(s)["display"])
        s = calculator.calculateNextState(s, "=")
        self.assertEqual('-2.9', json.loads(s)["display"])


if __name__ == "__main__":
    unittest.main()
