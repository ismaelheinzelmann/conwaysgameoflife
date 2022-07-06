import pygame
import sys
from grid import Grid

from colors import blue, red, orange, yellow, cream

display = pygame.display.set_mode((600, 600))

class ConwaysGame():

    def __init__(self):
        pass
    
    def input_handler(self, args):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def draw_dead(self, display, i, j):
        pygame.draw.rect(display, red, (30*i, 30*j, 30, 30))

    def draw_alive(self, display, i, j):
        pygame.draw.rect(display, orange, (30*i, 30*j, 30,30))

    def main(self):
        pygame.init()
        world = Grid(10)
        world.set_grid([[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,0,0,0,0],
                        [0,0,0,1,1,1,0,0,0,0],
                        [0,0,0,1,1,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]])           
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock = pygame.time.Clock()
            display.fill(blue)
            for i in range(len(world.grid)):
                for j in range(len(world.grid)):
                    if world.grid[i][j] == 1: self.draw_alive(display, i, j)
                    else: self.draw_dead(display, i, j)
            clock.tick(1)
            world.update_grid()
            pygame.display.flip()



            

game = ConwaysGame()
game.main()