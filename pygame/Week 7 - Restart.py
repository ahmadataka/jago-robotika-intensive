import pygame
import random
import time

# Initialize PyGame
pygame.init()

# Game Settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Obstacle Avoidance with Timer and Score")
font = pygame.font.Font(None, 36)

# Load images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
background_image = pygame.image.load("background.jpeg")

# Resize images
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
background_image = pygame.transform.scale(background_image, (800, 600))

# Load sound effects
win_sound = pygame.mixer.Sound("win.mp3")  # Replace with the path to your win sound file
lose_sound = pygame.mixer.Sound("lose.mp3")  # Replace with the path to your lose sound file

# Load background music
# pygame.mixer.music.load("background_music.mp3")
# pygame.mixer.music.play(-1, 0.0)  # Loop music indefinitely

# Game restart function
def restart_game():
    global player_x, player_y, enemies, enemy_rects, start_time, score, running
    player_x, player_y = 375, 275  # Reset player position
    score = 0  # Reset score
    start_time = time.time()  # Reset timer
    # Reset enemies to their starting positions
    enemies = [{"x": random.randint(50, 750), "y": random.randint(50, 550), "speed": 2} for _ in range(3)]
    enemy_rects = [enemy_image.get_rect(topleft=(enemy["x"], enemy["y"])) for enemy in enemies]
    running = True  # Restart the game loop

# Player settings
player_x, player_y = 375, 275
player_speed = 5
player_rect = player_image.get_rect(topleft=(player_x, player_y))  # Create player rectangle

# Enemy settings
enemies = [{"x": random.randint(50, 750), "y": random.randint(50, 550), "speed": 2} for _ in range(3)]
enemy_rects = [enemy_image.get_rect(topleft=(enemy["x"], enemy["y"])) for enemy in enemies]  # Enemy rectangles

# Timer and Score settings
start_time = time.time()
time_limit = 30  # seconds
score = 0

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Update the player rectangle position
    player_rect.topleft = (player_x, player_y)

    # Check for collision between player and enemies using bounding boxes
    for enemy_rect in enemy_rects:
        if player_rect.colliderect(enemy_rect):
            lose_sound.play()  # Play lose sound on collision
            print("Game Over!")
            restart_game()  # Restart the game when collision happens

    # Move the enemies randomly
    for enemy in enemies:
        enemy["x"] += random.choice([-enemy["speed"], 0, enemy["speed"]])
        enemy["y"] += random.choice([-enemy["speed"], 0, enemy["speed"]])

        # Keep enemy within screen bounds
        enemy["x"] = max(0, min(750, enemy["x"]))
        enemy["y"] = max(0, min(550, enemy["y"]))

    # Update the enemy rectangle positions
    enemy_rects = [enemy_image.get_rect(topleft=(enemy["x"], enemy["y"])) for enemy in enemies]

    # Time limit check
    elapsed_time = int(time.time() - start_time)
    time_left = time_limit - elapsed_time
    if time_left <= 0:
        print("Time's up! Final Score:", score)
        restart_game()  # Restart the game when the time is up

    # Check if player reaches the goal (simple condition for now)
    if player_x > 750 and player_y > 550:  # Target reached
        score += 10
        win_sound.play()  # Play win sound when target is reached
        print(f"Score: {score}, New Target!")
        restart_game()  # Restart the game after winning

    # Clear the screen and draw background
    screen.blit(background_image, (0, 0))

    # Draw the player and enemies
    screen.blit(player_image, (player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["x"], enemy["y"]))

    # Display score and timer
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    timer_text = font.render(f"Time Left: {time_left}s", True, (255, 255, 255))
    screen.blit(timer_text, (650, 10))

    pygame.display.update()

    # Frame rate control
    pygame.time.Clock().tick(60)

# Quit PyGame
pygame.quit()
