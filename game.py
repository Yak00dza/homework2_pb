import time

import options
import uinp
import random
from grid import Grid
from main import clear, main_menu

# Decimal codes of 180 human-recognizable utf8 chars. Capital X is excluded.
UTF8_RANGE = list(range(33, 88)) + list(range(945, 970)) + list(range(1040, 1066)) + list(range(1072, 1098)) + list(range(8592, 8610))

score = 0
total_chars = None

moves_made = 0

CARD_FLIP_DELAY = options.get_game_option('card_flip_delay')

def victory(moves_made):
    print(f'Congratulations! You won the game in {moves_made} moves!')
    input('Press ENTER to return to the main menu! ')

def random_grid(): 
    w = random.randint(1, options.MAX_GRID_W)
    l = random.randint(1, options.MAX_GRID_L)
    return Grid(w, l)

def generate_grid():
    if options.get_game_option('randomize_grid_size'):
        return random_grid()

    grid_size = options.get_game_option('static_grid_size')
    w, l = map(int, grid_size.split('x'))
    return Grid(w, l)

def get_tile_from_user(grid):
    hint = '(A1) '
    def check(value):
        if value == 'exit':
            return None
        try:
            y = ord(value[0].lower()) - 96 # a -> 1, b -> 2 ......
            x = int(value[1:])
        except:
            raise ValueError('Please try again')
        
        if not 0 <= x <= grid.width or not 0 <= y <= grid.length:
            raise ValueError('The coordinates are out of allowed range')
        
        tile = grid.get_tile(x, y)
        if tile.open:
            raise ValueError('The tile is already open')
        return tile
    return uinp.get_user_input(check, hint)

def generate_char(grid):
    randval  = random.random() #randval between 0 and 1
    threshhold = (grid.total_chars - grid.unique_chars) / grid.total_chars #randval below threshhold result in a new char
    if len(grid.present_chars) == 0:
        randval = 0
    if randval < threshhold:
        choice = random.choice(UTF8_RANGE)
        UTF8_RANGE.remove(choice)
        char = chr(choice)
        grid.present_chars.append(char)
        grid.unique_chars += 1
        return char
    char = random.choice(grid.present_chars)
    grid.present_chars.remove(char)
    return char
        

def reveal_tile(grid):
    tile = get_tile_from_user(grid)
    if tile is None:
        return tile
    tile.flip()

    if tile.char is None:
        tile.char = generate_char(grid)
    
    return tile

def loop(grid, score, moves_made):
    grid.display()
    tile1 = reveal_tile(grid)
    if tile1 == None: #leave the game if user decided so
        return
    clear()

    grid.display()
    tile2 = reveal_tile(grid)
    if tile2 == None: #leave the game if user decided so
        return
    clear()

    grid.display()
    
    new_score = score
    if tile1.char == tile2.char:
        new_score += 1
    else:
        time.sleep(CARD_FLIP_DELAY)
        tile1.flip()
        tile2.flip()
    if new_score == grid.total_chars:
        victory(moves_made)
        return

    clear()
    loop(grid, new_score, moves_made+1)    

def start():
    clear()
    grid = generate_grid()

    loop(grid, 0, 0)

