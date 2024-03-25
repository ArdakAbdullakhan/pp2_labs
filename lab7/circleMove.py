import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Moving circle")
screen.fill((255, 255, 255))

x = 400
y = 400
speed = 20

circle_color = (255,0, 0)
circle_position = (x, y)
circle_radius = 25

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_UP] and y-25>0:
        y -= speed
    if pressed_keys[pygame.K_DOWN] and y+25<800:
        y += speed
    if pressed_keys[pygame.K_LEFT] and x-25>0:
        x -= speed
    if pressed_keys[pygame.K_RIGHT] and x+25<800:
        x += speed

    #x = max(25, min(x, screen.get_width() - 25))
    #y = max(25, min(y, screen.get_height() - 25))
    circle_position = (x, y)
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)
    pygame.display.update()
    clock.tick(60)

