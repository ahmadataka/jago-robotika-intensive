import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the Enemy")

# Player settings
player_width = 50
player_height = 50
player_x = 375
player_y = 275
player_speed = 5

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 2

# Enemy initial position
enemy_x = random.randint(50, 750)
enemy_y = random.randint(50, 550)

# Game loop
running = True
font = pygame.font.Font(None, 36)  # Font for "Game Over" text
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed  # Move left
    if keys[pygame.K_RIGHT]:
        player_x += player_speed  # Move right
    if keys[pygame.K_UP]:
        player_y -= player_speed  # Move up
    if keys[pygame.K_DOWN]:
        player_y += player_speed  # Move down

    # Update enemy position (random movement)
    enemy_x += random.choice([-enemy_speed, 0, enemy_speed])  # Random horizontal movement
    enemy_y += random.choice([-enemy_speed, 0, enemy_speed])  # Random vertical movement

    # Check for collision with the enemy
    if (player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and player_y + player_height > enemy_y):
        screen.fill((0, 0, 0))  # Clear screen with black
        text = font.render("Game Over!", True, (255, 0, 0))  # Render "Game Over!" text
        screen.blit(text, (350, 250))  # Draw text at the center of the screen
        pygame.display.update()
        pygame.time.delay(2000)  # Delay before quitting the game
        running = False
        break

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

    # Draw the enemy
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_width, enemy_height))

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()
