import re
import json


def calculateNextState(json_state, input):

    json_state = json.loads(json_state)
    expression = ''
    end_of_exp = False

    if json_state is not None:
        expression = json_state.get('expression', '')
        end_of_exp = json_state.get('end_of_exp', False)

    if input == "=":
        display_number = float(eval(expression))

        end_of_exp = True
        expression = str(display_number)
    else:
        if input.isdigit() and end_of_exp == True:
            expression = input
        else:
            expression += input
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