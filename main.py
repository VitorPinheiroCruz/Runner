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
        return []

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

# Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))
obstacle_rect_list = []

# Player
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400,200))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Vc clicou no x')
            pygame.quit()
            exit()

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
            print('timer')

    if game_active:
        screen.blit(ground_surface, (0, 300))
        screen.blit(sky_surface, (0, 0))  # .blit(surface, position)
        score = display_score()

        # Player gravidade
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        if player_rect.colliderect(snail_rect):
            print('houve uma colisão com o snail')
            game_active = False
    else:
        snail_rect.left = 800
        start_time = pygame.time.get_ticks()
        screen.fill((94,129,162))
        name_game()
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
