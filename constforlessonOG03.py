import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра тир")
icon = pygame.image.load("IMG/234.jpg")

pygame.display.set_icon(icon)
target_img =pygame.image.load("IMG/target.png")
target_width = 100
target_height = 100
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0,255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass
pygame.quit()