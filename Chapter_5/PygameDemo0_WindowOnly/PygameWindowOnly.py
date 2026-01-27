# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys # handle special events like exit the program

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 # how many frames per second to update the screen

# 3 - Initialize the world
pygame.init() # automatically initializes all the pygame modules
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock() # oobject to help track time
 
# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
 
# 6 - Loop forever
while True: # end only by using sys.exit()

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8 - Do any "per frame" actions 
    
    # 9 - Clear the window
    window.fill(BLACK) # black background
    
    # 10 - Draw all window elements

    # 11 - Update the window
    pygame.display.update() # show the new window contents (otherwise the code above just stores them in memory)

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait (animation is 24-60 fps usually)
