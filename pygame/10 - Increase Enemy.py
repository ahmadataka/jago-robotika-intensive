import pygame
import random
import sys
import time

# Inisialisasi
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Level Naik = Musuh Bertambah")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Warna
WHITE = (255, 255, 255)

# Load gambar
player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
background = pygame.image.load("background.jpeg")
background = pygame.transform.scale(background, (800, 600))

# Player
player_x, player_y = 375, 275
player_speed = 5
player_rect = player_image.get_rect(topleft=(player_x, player_y))

# Enemy - list musuh awal
enemies = []

def tambah_musuh(jumlah):
    for _ in range(jumlah):
        x = random.randint(0, 750)
        y = random.randint(0, 550)
        speed_x = random.choice([-2, -1, 1, 2])
        speed_y = random.choice([-2, -1, 1, 2])
        enemies.append({"x": x, "y": y, "speed_x": speed_x, "speed_y": speed_y})

# Game State
start_time = time.time()
level = 1
waktu_per_level = 15  # detik
tambah_musuh(3)  # musuh awal

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    elapsed = int(time.time() - start_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Kontrol player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_y -= player_speed
    if keys[pygame.K_s]: player_y += player_speed
    if keys[pygame.K_a]: player_x -= player_speed
    if keys[pygame.K_d]: player_x += player_speed

    player_rect.topleft = (player_x, player_y)

    # Cek naik level
    if elapsed // waktu_per_level + 1 > level:
        level += 1
        tambah_musuh(2)  # Tambah musuh tiap level
        print(f"Naik ke Level {level}!")

    # Gambar dan gerakkan musuh
    for enemy in enemies:
        enemy["x"] += enemy["speed_x"]
        enemy["y"] += enemy["speed_y"]

        if enemy["x"] <= 0 or enemy["x"] >= 750:
            enemy["speed_x"] *= -1
        if enemy["y"] <= 0 or enemy["y"] >= 550:
            enemy["speed_y"] *= -1

        screen.blit(enemy_image, (enemy["x"], enemy["y"]))

        # Deteksi tabrakan
        enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 50, 50)
        if player_rect.colliderect(enemy_rect):
            print("Kena musuh! Game over!")
            running = False

    # Gambar player
    screen.blit(player_image, (player_x, player_y))

    # Tampilkan waktu & level
    timer_text = font.render(f"Time: {elapsed}s", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(timer_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(60)
