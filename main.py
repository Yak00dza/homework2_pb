import os
import game
import options
import uinp
from menu import Menu, MenuOption

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def leave():
    clear()
    print('Thanks for playing the memory game!')
    exit()

def main_menu():
    clear()
    menu = Menu()
    menu.add_option(MenuOption(game.start, 'Start the game'))
    menu.add_option(MenuOption(options.edit, 'Edit the game options'))
    menu.add_option(MenuOption(leave, 'Leave the game'))

    print('Welcome to the memory game!')
    menu.display()
    
    choice = menu.user_choice()
    choice.action()

def main():
    while True:
        main_menu()

if __name__ == '__main__':
    main()
