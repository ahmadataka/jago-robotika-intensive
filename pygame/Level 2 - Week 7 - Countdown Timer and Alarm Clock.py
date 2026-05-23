import pygame
pygame.init()

# Setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 7 - Countdown Timer")
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# Buttons
btn_start = pygame.Rect(100, 250, 120, 60)
btn_reset = pygame.Rect(250, 250, 120, 60)
btn_add = pygame.Rect(400, 250, 60, 60)
btn_minus = pygame.Rect(470, 250, 60, 60)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (60, 180, 60)
RED = (200, 60, 60)
BLUE = (80, 130, 255)

# Sounds
alarm = pygame.mixer.Sound("alarm.wav")

# Timer State
countdown_time = 10  # in seconds
start_time = 0
running = False
finished = False

# Main Loop
running_app = True
while running_app:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_app = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_start.collidepoint(event.pos):
                if not running and not finished:
                    running = True
                    start_time = pygame.time.get_ticks()
                elif finished:
                    finished = False
                    countdown_time = 10
            if btn_reset.collidepoint(event.pos):
                running = False
                countdown_time = 10
                finished = False
            if btn_add.collidepoint(event.pos) and not running:
                countdown_time += 5
            if btn_minus.collidepoint(event.pos) and not running:
                countdown_time = max(5, countdown_time - 5)

    # Logic
    if running and not finished:
        elapsed = (pygame.time.get_ticks() - start_time) / 1000
        remaining = 10 - int(elapsed)
        if remaining <= 0:
            running = False
            finished = True
            alarm.play()
        else:
            countdown_time = remaining

    # Draw
    screen.fill(WHITE)
    label = "Time's Up!" if finished else f"{countdown_time:02d}"
    color = RED if finished else BLACK
    text = font.render(label, True, color)
    screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//3)))

    # Buttons
    pygame.draw.rect(screen, GREEN, btn_start, border_radius=20)
    pygame.draw.rect(screen, BLUE, btn_reset, border_radius=20)
    pygame.draw.rect(screen, (100, 100, 255), btn_add, border_radius=10)
    pygame.draw.rect(screen, (100, 100, 255), btn_minus, border_radius=10)
    screen.blit(small_font.render("Start", True, WHITE), btn_start.move(25, 15))
    screen.blit(small_font.render("Reset", True, WHITE), btn_reset.move(25, 15))
    screen.blit(small_font.render("+", True, WHITE), btn_add.move(20, 10))
    screen.blit(small_font.render("-", True, WHITE), btn_minus.move(20, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()