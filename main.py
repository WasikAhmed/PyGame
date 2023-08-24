import pygame
import os

WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game!")

WHITE = (255, 255, 255)
FPS = 60
VELOCITY = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_screen(red, yellow):
    SCREEN.fill(WHITE)
    SCREEN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    SCREEN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def handle_yellow_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a]: # LEFT
        yellow.x -= VELOCITY
    if key_pressed[pygame.K_d]: # RIGHT
        yellow.x += VELOCITY
    if key_pressed[pygame.K_s]: # DOWN
        yellow.y += VELOCITY
    if key_pressed[pygame.K_w]: # UP
        yellow.y -= VELOCITY

def handle_red_movement(key_pressed, red):
    if key_pressed[pygame.K_j]: # LEFT
        red.x -= VELOCITY
    if key_pressed[pygame.K_l]: # RIGHT  
        red.x += VELOCITY
    if key_pressed[pygame.K_k]: # DOWN
        red.y += VELOCITY
    if key_pressed[pygame.K_i]: # UP
        red.y -= VELOCITY

def main():
    red = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            key_pressed = pygame.key.get_pressed()
            handle_yellow_movement(key_pressed, yellow)  
            handle_red_movement(key_pressed, red)  

        draw_screen(red, yellow)

    pygame.quit()       

if __name__ == "__main__":
    main()