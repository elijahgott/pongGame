# Example file showing a basic pygame "game loop"
import pygame
from entities.player import Player
from entities.ball import Ball

screen_width = 1280
screen_height = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0 # delta for time, time since last render i think
score = 0 # IMPLEMENT SCORE!!!

# create font
font = pygame.font.Font(None, 48)
text_surface = font.render(f"Score: {score}", True, "white")
text_rect = text_surface.get_rect()

# player object, set initial position
player = Player(screen_width / 2, screen_height - 25)

# ball object, set initial position
ball = Ball(screen_width / 2, screen_height / 3)

# MAIN LOOP
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    player.draw(screen, "white")
    ball.draw(screen, "white")
    # draw ui
    screen.blit(text_surface, text_rect)

    # USER INPUT
    player.move(screen_height, screen_width, dt)

    # HANDLE BALL MOVEMENT (pause)
    ball.move(screen_height, screen_width, dt)


    # HANDLE PLAYER AND BALL COLLISION
    if pygame.Rect.colliderect(player.rect, ball.rect):
        score += 1
        text_surface = font.render(f"Score: {score}", True, "white")
        text_rect = text_surface.get_rect()
        
        if ball.direction.y == 1:
            ball.direction.y = -1 # change direction to up
            ball.y = ball.y - 5 # ball gets stuck inside rectangle otherwise
        else:
            ball.direction.y = 1 # change direction to down
            ball.y = ball.y + 5 # ball gets stuck inside rectangle otherwise


    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()