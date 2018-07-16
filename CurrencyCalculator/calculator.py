import re
import json


def validate_input_data(input_data):
    pattern = re.compile("^[0-9-+*/.=]$")
    if not bool(pattern.match(input_data)):
        raise Exception('Invalid input')


def validate_full_expression(expression):
    pattern = re.compile("^(\d*\.?\d+)([-+*/](\d*\.?\d+))*$")
    if not bool(pattern.match(expression)):
        raise Exception('Invalid input')


def validate_partial_expression(expression):
    pattern = re.compile("^(\d*\.?\d+)([-+*/](\d*\.?\d+))*[-+*/.]?$")
    if not bool(pattern.match(expression)):
        raise Exception('Invalid input')


def calculate_expression(expression):
    try:
        result = eval(expression)
        return int(result) if result % 1 == 0 else result
    except:
        raise Exception('Invalid input')


def extract_last_number_occurrence(expression):
    pattern = re.compile(r'(\d*\.?\d+)\D*$')
    try:
        return pattern.search(expression).group(1)
    except:
        raise Exception('Invalid input')


def calculateNextState(json_state, input_data):
    validate_input_data(input_data)
    json_state = json.loads(json_state)

    expression = json_state['expression'] if json_state is not None and 'expression' in json_state else ''
    end_of_exp = json_state['end_of_exp'] if json_state is not None and 'end_of_exp' in json_state else False

    if input_data == "=":
        validate_full_expression(expression)
        display = str(calculate_expression(expression))
        expression = display
        end_of_exp = True
    else:
        if input_data.isdigit() and end_of_exp is True:
            expression = input_data
        else:
            expression += input_data
        validate_partial_expression(expression)
        end_of_exp = False
        display = extract_last_number_occurrence(expression)

    return json.dumps({'expression': expression, 'end_of_exp': end_of_exp, 'display': display})
