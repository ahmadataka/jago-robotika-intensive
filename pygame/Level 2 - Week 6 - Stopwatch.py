import pygame
pygame.init()

# Setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 6 - Stopwatch")
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# Button rectangles
btn_start = pygame.Rect(100, 250, 120, 60)
btn_stop  = pygame.Rect(250, 250, 120, 60)
btn_reset = pygame.Rect(400, 250, 120, 60)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (80, 130, 255)
RED   = (200, 60, 60)
GREEN = (60, 180, 60)

# Stopwatch state
running = False
start_time = 0
elapsed = 0

# Main loop
running_app = True
while running_app:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_app = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_start.collidepoint(event.pos):
                running = True
                start_time = pygame.time.get_ticks() - elapsed
            if btn_stop.collidepoint(event.pos):
                running = False
            if btn_reset.collidepoint(event.pos):
                running = False
                elapsed = 0

    # Update elapsed time
    if running:
        elapsed = pygame.time.get_ticks() - start_time

    # Convert ms → seconds
    seconds = elapsed / 1000

    # Draw screen
    screen.fill(WHITE)

    # Time text
    time_text = font.render(f"{seconds:0.2f}", True, BLACK)
    screen.blit(time_text, (230, 120))

    # Draw buttons
    pygame.draw.rect(screen, GREEN, btn_start)
    pygame.draw.rect(screen, RED, btn_stop)
    pygame.draw.rect(screen, BLUE, btn_reset)

    screen.blit(small_font.render("Start", True, WHITE), (btn_start.x + 25, btn_start.y + 15))
    screen.blit(small_font.render("Stop", True, WHITE),  (btn_stop.x + 35,  btn_stop.y + 15))
    screen.blit(small_font.render("Reset", True, WHITE), (btn_reset.x + 25, btn_reset.y + 15))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

   