import json
import main
import uinp
import sys
from menu import Menu, MenuOption

MAX_GRID_L = 26
MAX_GRID_W = 9
def static_grid_size():
    hint = '(WxL) '
    def check(value):
        value = value.split('x')
        if len(value) != 2:
            raise ValueError('Please, provide the data in a format of WxL. Example: 2x3')
        w, l = int(value[0]), int(value[1])
        if w%2 and l%2:
            raise ValueError('At least one parameter must be divisible by two. Please, try again.')
        if w <= 0 or l <= 0:
            raise ValueError('Parameters must be positive integers. Please, try again.')
        if w > MAX_GRID_W:
            raise ValueError(f'Maximum grid width is {MAX_GRID_W}')
        if l > MAX_GRID_L:
            raise ValueError(f'Maximum grid length is {MAX_GRID_L}')
        return 'x'.join(value)
    return uinp.get_user_input(check, hint)

def randomize_grid_size():
    true = ['1', 'true', 't']
    false = ['0', 'false', 'f']
    hint = f'({"|".join(true)} / {"|".join(false)}) ' 
    def check(value):
        if value.lower() in true:
            return True
        if value.lower() in false:
            return False
        raise ValueError('Please, try again')
    return uinp.get_user_input(check, hint)

def card_flip_delay():
    hint = '(1.5) '
    def check(value):
        try:
            if float(value) > 0:
                return float(value)
            raise ValueError()
        except:
            raise ValueError('Please, try again')
    return uinp.get_user_input(check, hint)
def change(option_title):
    option_name = option_title.split(': ')[0]
    print(f'Specify a new value for option {option_name}')
    new_value = getattr(sys.modules[__name__], option_name)()
    
    with open('options.json', 'r+') as file:
        data = json.load(file)
        data[option_name] = new_value
        file.seek(0)
        json.dump(data, file)
        file.truncate()

    edit() #back to the options screen

def edit():
    main.clear()
    print('Choose an option tou wat to edit.')
    with open('options.json', 'r') as file:
        data = json.load(file)
    
    menu = Menu()
    for i in data:
        menu.add_option(MenuOption(change, f'{i}: {data[i]}'))
    menu.add_option(MenuOption(None, 'Back to main menu'))

    menu.display()
    choice = menu.user_choice()
    
    if choice.title == 'Back to main menu':
        return

    choice.action(choice.title)

def get_game_option(option_name):
    with open('options.json', 'r') as file:
        data = json.load(file)
    return data[option_name]
