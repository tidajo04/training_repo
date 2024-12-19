######### Imports ############################################################
import json
with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)
######## DEFINE FUNCTIONS ####################################################
def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False
# rather than running all as a single loop, as suggested in the assignment,
# I made them into a few functions. the thought being,
# if this were a wider program, the process could be more easily reapeated.

def repeat_calc (answer=''): #allows repeat w/ less nesting (more readable?)
    if answer.upper() == 'Y':
        return calculator_function()
    elif answer.upper() == 'N':
        prompt(MESSAGES[language]['thank_goodbye'])
        return
    elif answer == '':
        prompt(MESSAGES[language]['yn_isblank'])
        answer = input()
        return repeat_calc(answer)
    else:
        prompt(MESSAGES[language]['invalid_yn'])
        return repeat_calc()

def calculator_function():
    prompt(MESSAGES[language]['input_num'][0])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES[language]['invalid_num'])
        number1 = input()

    prompt(MESSAGES[language]['input_num'][1])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES[language]['invalid_num'])
        number2 = input()

    prompt(MESSAGES[language]['input_op'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES[language]['invalid_op'])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)

    prompt(f'{MESSAGES[language]['result']} {output}')

    prompt(MESSAGES[language]['again_yn'])
    answer = input()
    repeat_calc(answer)

############################## START PROGRAM #################################
print(MESSAGES['en']['line_break'])

prompt("Language? English ('en') or 'Slacker ('sl')")
language = input()

while language not in ['en', 'sl']:
    prompt("invalid choice, please enter English ('en') or Slacker ('sl')")
    language = input()

prompt(MESSAGES[language]['welcome'])

calculator_function()

print(MESSAGES[language]['line_break'])
