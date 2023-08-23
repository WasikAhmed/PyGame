import pygame

WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game!")

WHITE = (255, 255, 255)

def draw_screen():
    SCREEN.fill(WHITE)
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_screen()

    pygame.quit()       

if __name__ == "__main__":
    main()