import pygame
import random
import time

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the Enemy with Levels")

# Player settings
player_width = 50
player_height = 50
player_x = 375
player_y = 275
player_speed = 5

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 2  # Start with slow enemies
enemy_x = random.randint(50, 750)
enemy_y = random.randint(50, 550)

# Goal settings
goal_width = 50
goal_height = 50
goal_x = random.randint(50, 750)
goal_y = random.randint(50, 550)

# Level and score settings
level = 1
score = 0
start_time = time.time()  # Timer starts when the game begins
time_limit = 30  # Set the time limit for the game in seconds

# Advanced Enemy AI settings
enemy_behavior = "random"  # "random" or "chase"

# Game loop
running = True
font = pygame.font.Font(None, 36)  # Font for displaying text
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

    # Enemy behavior (random or chase)
    if enemy_behavior == "random":
        enemy_x += random.choice([-enemy_speed, 0, enemy_speed])  # Random horizontal movement
        enemy_y += random.choice([-enemy_speed, 0, enemy_speed])  # Random vertical movement
    elif enemy_behavior == "chase":
        # Simple AI: Enemy moves towards the player
        if enemy_x < player_x:
            enemy_x += enemy_speed  # Move right
        elif enemy_x > player_x:
            enemy_x -= enemy_speed  # Move left
        if enemy_y < player_y:
            enemy_y += enemy_speed  # Move down
        elif enemy_y > player_y:
            enemy_y -= enemy_speed  # Move up

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

    # Check if the player reaches the goal
    if (player_x < goal_x + goal_width and player_x + player_width > goal_x and
        player_y < goal_y + goal_height and player_y + player_height > goal_y):
        score += 10  # Increase score when the player reaches the goal
        goal_x = random.randint(50, 750)  # Move the goal to a new random position
        goal_y = random.randint(50, 550)
        level += 1  # Increase the level when the player reaches the goal

        # Increase difficulty for the next level
        enemy_speed += 1  # Enemies move faster
        if level % 2 == 0:  # Change enemy behavior on certain levels
            enemy_behavior = "chase"  # Enemies will chase the player

    # Check if the time limit has been reached
    elapsed_time = int(time.time() - start_time)  # Calculate elapsed time
    if elapsed_time >= time_limit:
        screen.fill((0, 0, 0))  # Clear screen with black
        text = font.render(f"Time's Up! Final Score: {score}", True, (255, 255, 0))  # Display final score
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

    # Draw the goal
    pygame.draw.rect(screen, (0, 0, 255), (goal_x, goal_y, goal_width, goal_height))

    # Display the score, time, and level
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Draw score in the top-left corner

    time_left = time_limit - elapsed_time
    time_text = font.render(f"Time Left: {time_left}s", True, (255, 255, 255))
    screen.blit(time_text, (650, 10))  # Draw time in the top-right corner

    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (350, 10))  # Draw level in the top-center

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()
