import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Pong")
MIDDLEYELLOW = (237, 177, 131)
BLACK = (140, 72, 67)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 165, 120
VEL = 5
MAX_BULLETS = 3
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
BULLET_VEL = 7

YELLOW_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate \
    (pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_red.png")
RED_SPACESHIP = pygame.transform.rotate \
    (pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(MIDDLEYELLOW)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 25:  # down
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 25:  # down
        red.y += VEL

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
