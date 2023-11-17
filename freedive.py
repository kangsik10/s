import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 타이틀 설정
pygame.display.set_caption("Raccoon Avoidance Game")

# 너구리 설정
raccoon_size = 50
raccoon_speed = 10
raccoon = pygame.Rect(screen_width / 2 - raccoon_size / 2, screen_height - raccoon_size, raccoon_size, raccoon_size)

# 장애물 설정
obstacle_speed = 10
obstacles = [pygame.Rect(random.randint(0, screen_width - 20), random.randint(-900, 0), 20, 20) for _ in range(9)]  # 아홉 개의 장애물 생성

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 너구리 움직임
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and raccoon.left > 0:
        raccoon.x -= raccoon_speed
    if keys[pygame.K_RIGHT] and raccoon.right < screen_width:
        raccoon.x += raccoon_speed

    # 장애물 움직임
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.bottom > screen_height:
            obstacle.x = random.randint(0, screen_width - 20)
            obstacle.y = random.randint(-900, 0)

    # 충돌 검사
    for obstacle in obstacles:
        if raccoon.colliderect(obstacle):
            running = False  # 충돌 시 게임 종료

    # 화면 그리기
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, raccoon)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
