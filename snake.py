import pygame
import sys
import random

# Inițializarea Pygame
pygame.init()

# Dimensiuni fereastră
width = 400
height = 400

# Culori
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Crearea ferestrei
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Inițializarea Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15

# Inițializarea fructului
fruit_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
fruit_spawn = True

# Inițializarea direcției inițiale
direction = 'RIGHT'
change_to = direction

# Funcție pentru afișarea mesajului de sfârșit de joc
def message(text, color):
    font = pygame.font.Font('freesansbold.ttf', 25)
    msg = font.render(text, True, color)
    msgRect = msg.get_rect()
    msgRect.center = (width/2, height/2)
    win.blit(msg, msgRect)
    pygame.display.update()
    pygame.time.wait(1000)

# Funcție pentru gestionarea evenimentelor
def game_over():
    message("Ai pierdut! Apasă SPACE pentru a juca din nou sau ESC pentru a ieși.", red)
    pygame.display.update()

# Buclă principală
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Validare pentru schimbarea direcției
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Actualizare poziție Snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Creștere Snake
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

    fruit_spawn = True
    win.fill(black)

    for pos in snake_body:
        pygame.draw.rect(win, white, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(win, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Verificare pentru coliziune cu peretele sau cu propriul corp
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()
