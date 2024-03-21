import pygame
import sys
import math
import datetime
import os


"""righthand = pygame.image.load('rigth-hand.png')"""


bg = pygame.image.load('bg.png')


    
pygame.init()
width, height=800,800
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("simple clock")
clock = pygame.time.Clock()
FPS = 50

def print_text(text, position):
    font = pygame.font.SysFont("Castellar", 40, True, False)
    surface = font.render(text, True, (0,0,0))
    screen.blit(surface, position)

def convert_degrees_to_pygame(R, theta):
    y = math.cos(2*math.pi*theta/360)*R
    x = math.sin(2*math.pi*theta/360)*R
    return x+400, -(y-400)



def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour



        screen.fill((255,255,255))  
        screen.blit(bg,(0,0))
    
        
        
        
        #minute
        R = 350
        theta = (minute+second/60)*(360/60)
        pygame.draw.line(screen, (0, 0 , 0), (400,400), convert_degrees_to_pygame(R, theta), 5)
        
        #second
        R = 300
        theta = second*(360/60)
        pygame.draw.line(screen, (255, 0 , 0), (400, 400), convert_degrees_to_pygame(R, theta), 3)
        
        #hour
        R = 250
        theta = (hour+minute/60+second/3600)*(360/12)
    
        pygame.draw.line(screen, (0, 0 , 0), (400, 400), convert_degrees_to_pygame(R, theta), 5)

        
        pygame.display.update()
        clock.tick(FPS)


game()