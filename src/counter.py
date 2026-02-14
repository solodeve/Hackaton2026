"""
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 360, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: 
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)

import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))

couleur = (255, 0, 0) 

# Signature Rect(left, top, width, height) -> Rect
counter_rectangle = pygame.Rect(50, 50, 50, 50)
counter_rectangle.top_right = (600, 0) 

# Boucle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, couleur, counter_rectangle)

    pygame.display.flip()

pygame.quit()



import pygame
import sys

pygame.init()

largeur, hauteur = 600, 600
fenetre = pygame.display.set_mode((largeur, hauteur))

clock = pygame.time.Clock()
counter = 360 

BLANC = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenetre.fill(BLANC) # affichage
    pygame.display.flip() # mise à jour


pygame.quit()
sys.exit()
"""


import pygame
import sys

pygame.init()

# Affichage
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Cols
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Police
font = pygame.font.SysFont("Arial", 40)


compte_rebours = 100  
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == timer_event:
            if compte_rebours > 0:
                compte_rebours -= 1
            else:
                print("Vous avez péri !")
                pygame.time.set_timer(timer_event, 0)  # fin de temps

  
    screen.fill(WHITE)  

    rect_x, rect_y = 10, 10
    rect_width, rect_height = 100, 50
    timer_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    pygame.draw.rect(screen, BLACK, timer_rect, border_radius=10)

    text_surf = font.render(str(compte_rebours), True, WHITE)

    text_rect = text_surf.get_rect(center=timer_rect.center)
    screen.blit(text_surf, text_rect) # Dessiner surface sur une autre


    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
sys.exit()
 