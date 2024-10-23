class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = None
        self.open = False

    def display(self):
        return self.char if self.open else 'X'
    
    def flip(self):
        self.open = not self.open
class Grid:
    def __init__(self, width, length):
        self.grid = [[Tile(x, y) for y in range(1, length+1)] for x in range(1, width+1)]
        self.width = width
        self.length = length
        self.total_chars = (self.width * self.length) / 2
        self.unique_chars = 0
        self.present_chars = []

    def get_tile(self, x, y):
        return self.grid[x-1][y-1]

    def display(self):
        print(' '*2 + ' '.join([chr(65 + i) for i in range(self.length)]))
        for row in self.grid:
            print(f'{row[0].x} {" ".join(list(map(lambda x : x.display(), row)))}')
    
