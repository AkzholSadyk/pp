import pygame
import sys


pygame.init()




screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball")
white = (255, 255, 255)
red = (255, 0, 0)


ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed = 20


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y -= ball_speed

    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed

    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed

    

    ball_x = max(ball_radius, min(screen_width - ball_radius, ball_x))
    ball_y = max(ball_radius, min(screen_height - ball_radius, ball_y))

    
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    pygame.display.update()




    pygame.time.Clock().tick(30)
