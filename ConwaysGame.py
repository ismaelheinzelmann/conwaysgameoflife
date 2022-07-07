import pygame
from pygame.locals import K_ESCAPE, K_z, K_x, K_e, K_SPACE, K_r, K_h
from math import floor
import sys
from Grid import Grid
from colors import blue, red, orange, yellow, cream, black
from State import State
#https://pygame.readthedocs.io/en/latest/4_text/text.html
class ConwaysGame():

    def __init__(self):
        self.running = True
        self.counter = 0
        self.tickrate = 60
        self.tickaux = 1
        self.state = State("game")
        self.display = pygame.display.set_mode((1400, 900))
        self.world = Grid(30)
    
    def input_handler(self, event):
        if event.key == K_ESCAPE:
            self.running = False
        elif event.key == K_z:
            self.set_tickrate(-1)
        elif event.key == K_x:
            self.set_tickrate(1)
        elif event.key == K_e:
            self.state.set_creating()
        elif event.key == K_SPACE:
            self.state.set_evolving()
        elif event.key == K_r:
            self.world.reset_grid(30)
        elif event.key == K_h: self.state.switch_help()

    def click_handler(self):
        pos = pygame.mouse.get_pos()
        x, y = (floor(pos[0]/30),floor(pos[1]/30))
        if x < 30 and y < 30:
            print(x, y)
            self.world.switch_cell(y,x)
            pygame.display.flip()
    
    def set_tickrate(self, tick):
        s = self.tickaux+tick
        if s > 0 and s < 9:
            self.counter = 0
            self.tickaux += tick
            self.tickrate = floor(60/(s))
    
    def increase_tick(self, world):
        if self.counter < self.tickrate:
            self.counter += 1
        else:
            self.counter = 0
            world.update_grid()            

    def draw_dead(self, display, i, j, blocksize):
        pygame.draw.rect(display, blue, (blocksize*i, blocksize*j, blocksize, blocksize), 2)
    
    def render_grid(self, world):
        for i in range(len(world.grid)):
                for j in range(len(world.grid)):
                    size = 30
                    if world.grid[i][j] == 1: self.draw_alive(self.display, j, i, size)
                    else: self.draw_dead(self.display, j, i, size)

    def draw_alive(self, display, i, j,blocksize):
        pygame.draw.rect(display, blue, (blocksize*i, blocksize*j, blocksize, blocksize), 2)
        pygame.draw.rect(display, orange, ((blocksize*i)+2, (blocksize*j)+2, blocksize-2 ,blocksize-2 ))

    def main(self):
        pygame.init()
        pygame.display.set_caption("Conway's Game Of Life by Ismael Heinzelmann")
        self.set_tickrate(1)
        self.world.set_grid([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                            [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                            [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

        while self.running:
            clock = pygame.time.Clock()

            #Event handling in the tick start
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.input_handler(event)
                elif event.type == pygame.MOUSEBUTTONDOWN and self.state == "creating":
                    self.click_handler()
            
            self.display.fill(black)

            #Render zone
            if self.state == "game":
                self.render_grid(self.world)
                self.increase_tick(self.world)
            elif self.state == "creating": self.render_grid(self.world)

            if self.state.help:
                pass

            clock.tick(60)
            pygame.display.flip()
        pygame.quit()

game = ConwaysGame()
game.main()