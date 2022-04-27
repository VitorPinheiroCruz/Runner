import pygame
from sys import exit
# import random

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()  # estabelece os FPS
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))  # .render(text, AA, color)
score_rect = score_surf.get_rect(center=(400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))
# snail_x_pos = 600
# snail_y_pos = 270

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Vc clicou no x')
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:  # ler e imprime a posição do mouse
        #     print(event.pos)

        # ler e imprime se houve clique
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print('mouse down')

        # colisão pelo evento
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('colision')

    screen.blit(ground_surface, (0, 300))
    screen.blit(sky_surface, (0, 0))  # .blit(surface, position)
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    # pygame.draw.line(screen, 'blue', (0,0), pygame.mouse.get_pos(), 3) #desenhando uma linha
    # pygame.draw.ellipse(screen, 'gold', pygame.Rect(50,200,100,100))  # desenhando uma elípse
    screen.blit(score_surf, score_rect)
    # snail_x_pos -= 4
    # if snail_x_pos < -50:
    #     snail_x_pos = 800
    #     snail_y_pos = random.randint(270, 360)
    snail_rect.x -= 4
    if snail_rect.right < 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):   # .collidepoint((x,y))
    #     print('collision')
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())  # leitura do clique do mouse

    pygame.display.update()
    clock.tick(60)

    01:29:37
    08:58:00
