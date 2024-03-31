
import pygame, sys
from pygame.locals import *
import random, time
from random import randrange

pygame.init()
 
WIDTH = 400
HEIGHT = 600
FPS = 60
FramePerSec = pygame.time.Clock()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
sc.fill((0,0,0))

def restart_game():
    WHITE = (255, 255, 255)
 

    WIDTH = 400
    HEIGHT = 600
    SIZE = 50
    SPEED = 5
    font_end = pygame.font.SysFont('Arial', 46, bold=True)

    
    
    ra = pygame.image.load('race.jpg')
    race = pygame.transform.scale(ra, (WIDTH, HEIGHT))
    enemy = pygame.image.load('enemy2.jpg')
    player = pygame.image.load('player2.jpg')
    enemy2 = pygame.transform.scale(enemy, (54, 98))
    player2 = pygame.transform.scale(player, (54, 98))

    pygame.display.set_caption("racer")

    apple = randrange(0, WIDTH, SIZE), randrange(0, WIDTH, SIZE)


 


    class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.coin = pygame.draw.circle(sc, pygame.Color('yellow'), apple, 20 )
        self.image = enemy2
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,WIDTH-40), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

      def coin(self):
          pass
 
 
    class Player(pygame.sprite.Sprite):
        def __init__(self):
         super().__init__() 
         self.image = player2
         self.rect = self.image.get_rect()
         self.rect.center = (160, 520)
        
        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP]:
               self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
             self.rect.move_ip(0,5)
         
            if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
            if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
      
    P1 = Player()
    E1 = Enemy()


    enemies = pygame.sprite.Group()
    enemies.add(E1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
 

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)
 

    while True:
       
    
        for event in pygame.event.get():
            if event.type == INC_SPEED:
              SPEED += 0.5
           
            if event.type == QUIT:
              pygame.quit()
              sys.exit()
            if event.type == K_1:
                       
              restart_game()
    


        sc.fill(WHITE)
        sc.blit(race, (0,0))
    

   
        for entity in all_sprites:
           sc.blit(entity.image, entity.rect)
           entity.move()
 
    
        if pygame.sprite.spritecollideany(P1, enemies):
          sc.fill((0,0,0))
          render_end = font_end.render('GAME OVER', 1, pygame.Color('white'))
          sc.blit(render_end, (HEIGHT //2 -250, WIDTH//2 + 50))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
        
        
          
       
         
        pygame.display.update()
        FramePerSec.tick(FPS)



restart_game()