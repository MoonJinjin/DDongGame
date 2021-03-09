import pygame
import random
import os

pygame.init() # 초기화

# pygame에 사용되는 전역변수 선언

background = pygame.image.load("C:/pythonworkspace/pygame_basic/paper.jpg")
size = [500, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DDDDDong Game")

running = True
clock = pygame.time.Clock()

def runGame():
    ddong_image = pygame.image.load("C:/pythonworkspace/pygame_basic/ddong.png")
    ddong_image = pygame.transform.scale(ddong_image, (60, 60))
    ddongs = []

    person_image = pygame.image.load("C:/pythonworkspace/pygame_basic/character.png")
    person_image = pygame.transform.scale(person_image, (100, 100))
    person = pygame.Rect(person_image.get_rect())
    person.left = size[0] // 2 - person.width // 2
    person.top = size[1] - person.height
    person_speed = 0

    for i in range(6):
        rect = pygame.Rect(ddong_image.get_rect())
        rect.left = random.randint(0, size[0]) # 0 ~ 600 랜덤 x좌표
        rect.top = -100
        speed = random.randint(4, 10) # 똥이 떨어지는 속도
        ddongs.append({'rect': rect, 'speed': speed})

    global running
    while running:
        clock.tick(30)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_speed = -5
                elif event.key == pygame.K_RIGHT:
                    person_speed = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_speed = 0
                elif event.key == pygame.K_RIGHT:
                    person_speed = 0

        for ddong in ddongs:
            ddong['rect'].top += ddong['speed']
            if ddong['rect'].top > size[1]:
                ddongs.remove(ddong)
                rect = pygame.Rect(ddong_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                speed = random.randint(3, 10)
                ddongs.append({'rect': rect, 'speed': speed})

        person.left = person.left + person_speed

        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width

        screen.blit(person_image, person)

        for ddong in ddongs:
            if ddong['rect'].colliderect(person):
                running = False
            screen.blit(ddong_image, ddong['rect'])

        pygame.display.update()


runGame()
pygame.quit()