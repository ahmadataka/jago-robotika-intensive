import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Box")

# Initial position of the player
player_x = 375
player_y = 275
player_width = 50
player_height = 50
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))  # Draw player
    pygame.display.update()  # Update the display

pygame.quit()
