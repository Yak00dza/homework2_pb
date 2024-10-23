# The memory game

# How to play?
The game loop is as follows:
1) You pick a card and it becomes flipped.
2) You pick another card.
3) If the cards you have chosen have the same character on them, they stay open for the rest of the game
4) Else, both cards are flipped after a short period of time

# What do the game options do?
1) `static_grid_size`  
This option determines the size of the grid. It is inputed in a format of WxL. Example `3x6`. One of the two numbers must be even. The maximal grid size is 9x26.
2) `randomize_grid`  
This option can be either true or false. If it is true, it overrides the `static_grid_size` and the grid has a random size each time you start playing.
3) `card_flip_delay`  
This option determines for how many seconds is the second card shown if it does not match the first one. This options could be any positive number.
