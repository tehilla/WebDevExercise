import re
import json


def calculateNextState(json_state, input_data):

    json_state = json.loads(json_state)
    expression = ''
    end_of_exp = False

    if json_state is not None:
        expression = json_state['expression'] if 'expression' in json_state else ''
        end_of_exp = json_state['end_of_exp'] if 'end_of_exp' in json_state else False

    if input_data == "=":
        display_number = float(eval(expression))

        end_of_exp = True
        expression = str(display_number)
    else:
        if input_data.isdigit() and end_of_exp == True:
            expression = input_data
        else:
            expression += input_data
        end_of_exp = False
        display_number = float(re.search(r'(\d*\.?\d+)\D*$', expression).group(1))

    display = str(int(display_number)) if display_number == int(display_number) else str(display_number)

    return json.dumps({'expression': expression, 'end_of_exp':end_of_exp, 'display': display})


def main():
    s = '{}'
    s = calculateNextState(s, "1")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "2")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "+")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "4")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "3")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "=")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "+")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "1")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "=")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "5")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "=")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "+")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "4")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "3")
    print(json.loads(s)["display"])
    s = calculateNextState(s, "=")
    print(json.loads(s)["display"])


if __name__ == "__main__":
    main()