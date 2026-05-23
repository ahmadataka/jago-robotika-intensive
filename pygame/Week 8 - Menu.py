import pygame
import sys
import random
import time

# Inisialisasi pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game dengan Menu")
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Gambar
player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
background_image = pygame.image.load("background.jpeg")
background_image = pygame.transform.scale(background_image, (800, 600))

# Suara
win_sound = pygame.mixer.Sound("win.mp3")
lose_sound = pygame.mixer.Sound("lose.mp3")
#pygame.mixer.music.load("background_music.mp3")
#pygame.mixer.music.play(-1)

# Fungsi untuk menampilkan teks
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, rect)

# Fungsi menu utama
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Selamat Datang di Game!", font, WHITE, screen, 400, 200)
        draw_text("Tekan ENTER untuk Mulai", small_font, WHITE, screen, 400, 300)
        draw_text("Tekan ESC untuk Keluar", small_font, WHITE, screen, 400, 350)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Masuk ke game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

# Fungsi utama game
def run_game():
    player_x, player_y = 375, 275
    player_speed = 5
    player_rect = player_image.get_rect(topleft=(player_x, player_y))
    enemies = [{"x": random.randint(50, 750), "y": random.randint(50, 550), "speed": 2} for _ in range(3)]
    score = 0
    start_time = time.time()
    time_limit = 30

    running = True
    while running:
        screen.blit(background_image, (0, 0))
        elapsed_time = int(time.time() - start_time)
        time_left = time_limit - elapsed_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player_y -= player_speed
        if keys[pygame.K_s]: player_y += player_speed
        if keys[pygame.K_a]: player_x -= player_speed
        if keys[pygame.K_d]: player_x += player_speed

        player_rect.topleft = (player_x, player_y)

        # Gambar player
        screen.blit(player_image, (player_x, player_y))

        # Update dan gambar musuh
        for enemy in enemies:
            enemy["x"] += random.choice([-enemy["speed"], 0, enemy["speed"]])
            enemy["y"] += random.choice([-enemy["speed"], 0, enemy["speed"]])
            enemy["x"] = max(0, min(750, enemy["x"]))
            enemy["y"] = max(0, min(550, enemy["y"]))
            screen.blit(enemy_image, (enemy["x"], enemy["y"]))
            if player_rect.colliderect(pygame.Rect(enemy["x"], enemy["y"], 50, 50)):
                lose_sound.play()
                return  # Kembali ke menu

        if player_x > 750 and player_y > 550:
            score += 10
            win_sound.play()
            return  # Kembali ke menu

        # Tampilkan skor dan waktu
        timer_text = small_font.render(f"Time Left: {time_left}", True, WHITE)
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        screen.blit(timer_text, (650, 10))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

# Program utama
while True:
    main_menu()
    run_game()
