import math
import time

import pygame

W = 1920
H = 1080
RW = 390
RH = 330

ratio_x = W/RW
ratio_y = H/RH

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
radar = pygame.surface.Surface(size=[RW, RH])
all_sprites = pygame.sprite.Group()

running = True

h_shift = 20
v_shift = 20
text_space = 100

player = pygame.math.Vector2()
enemy = pygame.math.Vector2()

player.update(0,5)
enemy.update(1, 11)
print(enemy.normalize())
enemy.update(1, 10)
print(enemy.normalize())
direction_player_to_enemy = (enemy-player).normalize()
print(direction_player_to_enemy)
print(90 + math.degrees(math.atan2(direction_player_to_enemy.y, direction_player_to_enemy.x)))
player.update(W/2-100, H-100)
while running:

    t = time.perf_counter()

    player.update(W/2-100, H-99)
    enemy.update(W/2, t*75)
    angle = enemy.angle_to(player)
    direction_player_to_enemy = (enemy - player).normalize()
    angle = 90 + math.degrees(math.atan2(direction_player_to_enemy.y, direction_player_to_enemy.x))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    screen.blit(radar, [1500, 720])

    font = pygame.font.SysFont("comicsansms", 10)

    deg_list = ["180", "210", "240", "270", "300", "330", "000", "030", "060", "090", "120", "150", "180"]
    for idx, val in enumerate(range(0, 390, 30)):
        pygame.draw.line(radar, WHITE, (15 + val, 0 + 30), (15 + val, RH - 35), 1)
        radar.blit(font.render(deg_list[idx], True, (0, 128, 0)), (val + 7.5, 10))
    pygame.draw.line(radar, WHITE, (15, 45), (RW - 15, 45),  1)
    pygame.draw.line(radar, WHITE, (15, 105), (RW - 15, 105), 1)
    pygame.draw.line(radar, WHITE, (15, 165), (RW - 15, 165), 1)
    pygame.draw.line(radar, WHITE, (15, 235), (RW - 15, 235), 1)
    print(enemy.x, enemy.y)
    pygame.draw.circle(radar, RED, (enemy.x/ratio_x + angle, enemy.y/ratio_y), 1, 0)

    pygame.draw.circle(screen, RED, (enemy.x, enemy.y), 5, 0)
    pygame.draw.circle(screen, RED, (player.x, player.y), 5, 0)

    pygame.display.flip()

pygame.quit()
