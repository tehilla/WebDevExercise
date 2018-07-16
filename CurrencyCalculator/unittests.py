import unittest
import calculator
import json


class CalculatorTests(unittest.TestCase):

    def test_calculateNextState_empty(self):
        with self.assertRaises(Exception):
            calculator.calculateNextState('{}', "-")

    def test_calculateNextState_add(self):
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

    def test_calculateNextState_minus(self):
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

    def test_calculateNextState_multiple(self):
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

    def test_calculateNextState_division(self):
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

    def test_calculateNextState_neg(self):
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

    def test_calculateNextState_float(self):
        s = calculator.calculateNextState(json.dumps({'expression': '1.2-2', 'end_of_exp': False, 'display': '2.1'}), "=")
        self.assertEqual('-0.8', json.loads(s)["display"])

    def test_validate_full_expression(self):
        calculator.validate_full_expression('2+3')
        calculator.validate_full_expression('2+3+5')

    def test_validate_full_expression_fail(self):
        with self.assertRaises(Exception):
            calculator.validate_full_expression('2+-3')

    def test_validate_partial_expression(self):
        calculator.validate_partial_expression('2')
        calculator.validate_partial_expression('2.3+')
        calculator.validate_partial_expression('2+3*')

    def test_validate_partial_expression_fail(self):
        with self.assertRaises(Exception):
            calculator.validate_partial_expression('2+-')
        with self.assertRaises(Exception):
            calculator.validate_partial_expression('2.*4')

    def test_extract_last_number_occurrence(self):
        self.assertEqual('2', calculator.extract_last_number_occurrence('34+93-28.6/2'))
        self.assertEqual('28.6', calculator.extract_last_number_occurrence('34+93-28.6'))
        self.assertEqual('93', calculator.extract_last_number_occurrence('34+93-*/+='))

    def test_extract_last_number_occurrence_with_fail(self):
        with self.assertRaises(Exception):
            calculator.extract_last_number_occurrence('+-')
        with self.assertRaises(Exception):
            calculator.extract_last_number_occurrence('')

    def test_validate_input_data(self):
        calculator.validate_input_data('2')
        calculator.validate_input_data('-')
        calculator.validate_input_data('+')
        calculator.validate_input_data('.')
        calculator.validate_input_data('=')
        calculator.validate_input_data('/')

    def test_validate_input_data_with_fail(self):
        with self.assertRaises(Exception):
            calculator.validate_input_data('@')
        with self.assertRaises(Exception):
            calculator.validate_input_data('19')
        with self.assertRaises(Exception):
            calculator.validate_input_data('?')
        with self.assertRaises(Exception):
            calculator.validate_input_data('**')
        with self.assertRaises(Exception):
            calculator.validate_input_data('+-')


if __name__ == "__main__":
    unittest.main()
