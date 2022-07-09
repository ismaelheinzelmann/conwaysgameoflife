import pygame
from pygame.locals import K_ESCAPE, K_z, K_x, K_e, K_SPACE, K_r, K_h
from math import floor
from Grid import Grid
from colors import blue, orange, black
from State import State

#https://pygame.readthedocs.io/en/latest/4_text/text.html
#TODO Implementar escritas à direita
#TODO Implementar interface com status
#TODO Implementar DEMOS
#TODO Implementar Explicação

pygame.font.init()
Font = pygame.font.SysFont("Arial", 30)
class ConwaysGame():

    def __init__(self):
        self.running = True
        self.counter = 0
        self.tickrate = 10
        self.state = State("creating")
        self.display = pygame.display.set_mode((1500, 1000))
        self.n = 50
        self.world = Grid(self.n)
        self.size = 20
    
    def input_handler(self, event):
        if event.key == K_ESCAPE:
            self.running = False
        elif event.key == K_x:
            self.set_tickrate(-1)
        elif event.key == K_z:
            self.set_tickrate(1)
        elif event.key == K_e:
            self.world.grid = self.world.start_grid
            self.state.set_creating()
        elif event.key == K_SPACE:
            self.world.start_grid = self.world.grid
            self.state.set_evolving()
        elif event.key == K_r:
            self.state.set_creating()
            self.world.reset_grid(self.n)
        elif event.key == K_h: self.state.switch_help()

    def click_handler(self):
        pos = pygame.mouse.get_pos()
        x, y = (floor(pos[0]/self.size),floor(pos[1]/self.size))
        if x < self.n and y < self.n:
            self.world.switch_cell(y,x)
    
    def set_tickrate(self, tick):
        s = self.tickrate + tick * 5
        if s <= 60 and s > 0:
            self.tickrate = s
    def increase_tick(self, world):
        if self.counter <= self.tickrate:
            self.counter += 1
        else:
            self.counter = 0
            world.update_grid()

    def draw_dead(self, display, i, j, blocksize):
        pygame.draw.rect(display, blue, (blocksize*i, blocksize*j, blocksize, blocksize), 2)
    
    def render_grid(self, world):
        for i in range(len(world.grid)):
                for j in range(len(world.grid)):
                    if world.grid[i][j] == 1: self.draw_alive(self.display, j, i, self.size)
                    else: self.draw_dead(self.display, j, i, self.size)

    def draw_alive(self, display, i, j,blocksize):
        pygame.draw.rect(display, blue, (blocksize*i, blocksize*j, blocksize, blocksize), 2)
        pygame.draw.rect(display, orange, ((blocksize*i)+2, (blocksize*j)+2, blocksize-2 ,blocksize-2 ))

    #main game routine
    def main(self):
        pygame.init()
        pygame.display.set_caption("Conway's Game Of Life by Ismael Heinzelmann")
        COMMANDS = pygame.image.load("imgs/comandos.png")
        RULES = pygame.image.load("imgs/regras.png")
        CREATING = pygame.image.load("imgs/criandomundo.png")
        EVOLVING = pygame.image.load("imgs/evoluindo.png")

        while self.running:
            clock = pygame.time.Clock()
            self.display.fill(black)
            self.display.blit(COMMANDS, (1000, 200)) 
            self.display.blit(RULES, (1000, 600))

            #Event handling in the tick start
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.input_handler(event)
                elif event.type == pygame.MOUSEBUTTONDOWN and self.state == "creating":
                    self.click_handler()

            #Render zone
            if self.state == "game":
                self.render_grid(self.world)
                self.display.blit(EVOLVING, (1000, -10))                

                self.increase_tick(self.world)
            elif self.state == "creating":
                self.render_grid(self.world)
                self.display.blit(CREATING, (1000, 0))
            
            clock.tick(60)
            pygame.display.flip()
        pygame.quit()

game = ConwaysGame()
game.main()