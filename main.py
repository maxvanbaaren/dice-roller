import PySimpleGUI as sg
import random

# types of dice
dice_list = ['d2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

# window theme
sg.theme('LightPurple')

# window contents
layout = [[sg.Combo(dice_list, key='combo', default_value='d20'), sg.Input(key='input')],
          [sg.Text(size=(40, 1), key='output')],
          [sg.Text(size=(40, 1), key='total')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# create the window
window = sg.Window('Dice Roller', layout)

# display and interact with the window using an Event Loop
while True:
    event, values = window.read()

    # checks if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # checks if user entered int
    try:
        int(values['input'])
    except ValueError:
        window['output'].update("Please enter a valid number")
        window['total'].update("")
        continue

    results = [0] * int(values['input'])  # array of die rolls
    results_string = ""  # string of die rolls
    die_max = int(values['combo'][1:])  # maximum value that can be rolled

    # adds rolls to results/results_string
    for i in range(0, len(results)):
        results[i] = random.randint(1, die_max)
        results_string += str(results[i]) + " "
        if i == len(results)-1:
            results_string += "= "
        else:
            results_string += "+ "

    total = sum(results)  # sum of all rolls

    # update window with results message
    window['output'].update('Rolling ' + values['input'] + " " + values['combo'] + ": " + results_string)
    window['total'].update("Total: " + str(total))

# close window
window.close()
