import pygame
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'Score: {current_time / 1000:.2f}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            screen.blit(snail_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return  []

def game_message():
    text_font = pygame.font.Font('font/Pixeltype.ttf', 30)
    text = text_font.render("Don't hit the snail; Press space to jump over it. ;-)", False, (111, 196, 169))
    text_rect = text.get_rect(center=(400, 320))
    screen.blit(text, text_rect)

def name_game():
    game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center=(400, 80))
    screen.blit(game_name, game_name_rect)

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My game Runner')
clock = pygame.time.Clock()  # estabelece os FPS
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64,64))  # .render(text, AA, color)
# score_rect = score_surf.get_rect(center=(400,50))

# Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))
# snail_x_pos = 600
# snail_y_pos = 270

obstacle_rect_list = []



player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
# # player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400,200))

# player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
# player_stand_scaled = pygame.transform.scale(player_stand, (200, 400))
# player_stand_rect = player_stand_scaled.get_rect(center=(400,200))
# # player_stand_rect = player_stand.get_rect(midbottom=(400,200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Vc clicou no x')
            pygame.quit()
            exit()
        # solução do desenvolver para recomeçar o jogo
        # habilidade de pular quando o mouse clica no player - my design
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -20

            # habilidade de pular pressionando o space
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            # após game over, recomeçar o jogo pressionando o espaço
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: game_active = True

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
            # print('test')

        # # habilidade de pular quando o mouse clica no player - my design
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #         if player_rect.bottom >= 300:
        #             player_gravity = -20
        #
        # # habilidade de pular pressionando o space
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
        #         player_gravity = -20
        #
        # # após game over, recomeçar o jogo pressionando o espaço
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE: game_active = True

        # print jump toda vez que a tecla space é pressionada
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print('jump')

        # print key-down toda vez que uma tecla é pressionada
        # print key-up toda vez que uma tecla é pressionada
        # if event.type == pygame.KEYDOWN:
        #     print('key-down')
        # if event.type == pygame.KEYUP:
        #     print('key-up')

        # if event.type == pygame.MOUSEMOTION:  # ler e imprime a posição do mouse
        #     print(event.pos)

        # ler e imprime se houve clique
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print('mouse down')

        # colisão pelo evento
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    if game_active:
        screen.blit(ground_surface, (0, 300))
        screen.blit(sky_surface, (0, 0))  # .blit(surface, position)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()
        # pygame.draw.line(screen, 'blue', (0,0), pygame.mouse.get_pos(), 3) #desenhando uma linha
        # pygame.draw.ellipse(screen, 'gold', pygame.Rect(50,200,100,100))  # desenhando uma elípse
        # snail_x_pos -= 4
        # if snail_x_pos < -50:
        #     snail_x_pos = 800
        #     snail_y_pos = random.randint(270, 360)
        # snail_rect.x -= 4
        # if snail_rect.right < 0: snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)

        # Player gravidade
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        # colocando gravidade do player
        screen.blit(player_surf, player_rect)
        # screen.blit(player_surf, (player_rect[0], player_rect[1] + player_gravity))
        # screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)




        # if player_rect.colliderect(snail_rect):
        #     print('collision')
        # print jump toda vez que a tecla spaço é pressionada
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):   # .collidepoint((x,y))
        #     print('collision')
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())  # leitura do clique do mouse

        # Collision
        if player_rect.colliderect(snail_rect):
            print('houve uma colisão com o snail')
            game_active = False
            # pygame.quit()
            # exit()
    else:
        snail_rect.left = 800
        start_time = pygame.time.get_ticks()
        screen.fill((94,129,162))
        name_game()
        # screen.fill('yellow')
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(f'You score: {score/1000:.2f}',False, (111,196,169))
        score_message_rect = score_message.get_rect(center=(400,330))
        if score == 0:
            game_message()
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)

# 02:01:28
# 02:38:23
