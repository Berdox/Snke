import pygame
from pygame.locals import *
from Game import *
import time
import random

SIZE = 40
HEIGHT = 1000
WIDTH = 800

class Item:
    def __init__(self, location, x ,y, parent_Screen):
        self.loc = location
        self.x = x
        self.y = y
        self.parent_screen = parent_Screen
        
        
class Apple(Item):
    def __init__(self, location, x, y, parent_screen):
        super().__init__(location, x, y, parent_screen)
        self.x = SIZE * 3
        self.y = SIZE * 3
    
    def move(self):
        self.x = random.randint(0,24) * SIZE
        self.y = random.randint(0,19) * SIZE

class Snake(Item):
    def __init__(self, location, x, y, parent_screen, length):
        super().__init__(location, x, y, parent_screen)
        self.direction = 'right'
        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length
    
    def moveUp(self):
        self.direction = 'up'
    
    def moveDown(self):
        self.direction = 'down'
    
    def moveLeft(self):
        self.direction = 'left'
    
    def moveRight(self):
        self.direction = 'right'
        
    def moving(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        if(self.direction == 'up'):
            self.y[0] -= SIZE
            
        elif(self.direction == 'down'):
            self.y[0] += SIZE
        
        elif(self.direction == 'left'):
            self.x[0] -= SIZE
            
        elif(self.direction == 'right'):
            self.x[0] += SIZE
    
    def increaseLength(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        

class Game:
    def __init__(self):
        self.running = False
        self.surface = pygame.display.set_mode((HEIGHT, WIDTH))
    
    def stop(self):
        self.running = False
        
    def startup(self):
        pygame.init()
        self.surface.fill((125, 2, 153))
        pygame.display.flip()
        self.running = True

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        return False
        
    def run(self, instance):
        pygame.init()
        self.surface.fill((125, 2, 153))
        pygame.display.flip()
        
        loc = pygame.image.load("./resources/block.jpg").convert()
        x = 50
        y = 50
        snke = Snake(loc, x, y, self.surface, 6)
    
        locA = pygame.image.load("./resources/apple.jpg").convert()
        xA = 50
        yA = 50
        apple = Apple(locA, xA, yA, self.surface)
        itemL = [snke, apple]
        instance.redraw(itemL[0], 1)
        instance.redraw(itemL[1], 0)
        print(itemL[1])
        print(itemL[0].x)
    
        while instance.running:
            if self.is_collision(itemL[0].x[0], itemL[0].y[0], itemL[1].x, itemL[1].y):
                itemL[1].move()
                itemL[0].increaseLength()
            itemL[0].moving()
            instance.redraw(itemL[0], 1)
            instance.redraw(itemL[1], 0)
            instance.control(itemL)
            time.sleep(0.1)
    
        
    def redraw(self, image, snk):
        
        if snk == 1:
            image.parent_screen.fill((125, 2, 153))
            for i in range(image.length):
                image.parent_screen.blit(image.loc, (image.x[i], image.y[i]))
        else:
            image.parent_screen.blit(image.loc, (image.x, image.y))
        pygame.display.flip()
        
    def control(self, itemL):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    self.stop()
                    
                if event.key == K_UP:
                    itemL[0].moveUp()
                
                if event.key == K_DOWN:
                    itemL[0].moveDown()
                
                if event.key == K_LEFT:
                    itemL[0].moveLeft()
                    
                if event.key == K_RIGHT:
                    itemL[0].moveRight()
                    
            elif event.type == quit:
                self.stop()
        