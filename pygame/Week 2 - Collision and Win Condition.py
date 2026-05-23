import pygame
import random

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision and Win Condition")

# Player settings
player_width = 50
player_height = 50
player_x = 375  # Start position (center of the screen)
player_y = 275
player_speed = 1  # How fast the player moves

# Goal settings
goal_width = 50
goal_height = 50
goal_x = random.randint(50, 750)  # Random x position for the goal
goal_y = random.randint(50, 550)  # Random y position for the goal

# Game loop
running = True
font = pygame.font.Font(None, 36)  # Font for "You Win!" text
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

    # Check if player collides with the goal
    if (player_x < goal_x + goal_width and player_x + player_width > goal_x and
        player_y < goal_y + goal_height and player_y + player_height > goal_y):
        # Player has reached the goal
        screen.fill((0, 0, 0))  # Clear screen with black
        text = font.render("You Win!", True, (255, 255, 255))  # Render "You Win!" text
        screen.blit(text, (350, 250))  # Draw text at the center of the screen
    else:
        # Fill the screen with black
        screen.fill((0, 0, 0))
        
        # Draw the player as a green rectangle
        pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

        # Draw the goal as a red rectangle
        pygame.draw.rect(screen, (255, 0, 0), (goal_x, goal_y, goal_width, goal_height))

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()
