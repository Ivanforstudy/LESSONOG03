
import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра: Попади в цель")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Настройки игры
score = 0
target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)
target_speed = 5

# Главный игровой цикл
running = True
clock = pygame.time.Clock()  # Создание объекта Clock для ограничения FPS
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка нажатия мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Проверка попадания по цели
            if (mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2 <= target_radius ** 2:
                score += 1
                print(f"Очки: {score}")
                # Перемещение цели на новое случайное место
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)

    # Движение цели
    target_x += target_speed
    if target_x + target_radius > WIDTH or target_x - target_radius < 0:
        target_speed = -target_speed  # Изменить направление движения

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (target_x, target_y), target_radius)
    pygame.display.flip()

    # Ограничение кадров в секунду
    clock.tick(60)



