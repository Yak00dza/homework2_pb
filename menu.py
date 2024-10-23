import uinp

class MenuOption:
    def __init__(self, action, title):
        self.action = action
        self.title = title

class Menu:
    def __init__(self):
        self.storage = []
    
    def add_option(self, option):
        self.storage.append(option)

    def get_option(self, n):
        return self.storage[n-1]
    
    def get_menu_option_validator(self):
        def validator(value):
            if int(value) in range(1, len(self.storage)+1):
                return int(value)
            raise ValueError('Incorrect menu option provided')
        return validator

    def user_choice(self):
        return self.get_option(
        uinp.get_user_input(
            self.get_menu_option_validator(),
            f'({"/".join([str(i) for i in range(1, len(self.storage)+1)])}) '
        )
    )
  

    def display(self):
        for i in range(len(self.storage)):
            print(f'{i+1}. {self.storage[i].title}')
    
