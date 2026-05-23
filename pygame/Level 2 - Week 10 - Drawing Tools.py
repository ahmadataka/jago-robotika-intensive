import pygame
pygame.init()

# Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 9 - Drawing Shapes Tool")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (80,130,255)
RED = (200,60,60)
GREEN = (60,180,60)
GRAY = (200,200,200)

# Tombol mode
btn_line = pygame.Rect(50, 20, 100, 40)
btn_rect = pygame.Rect(200, 20, 100, 40)
btn_circle = pygame.Rect(350, 20, 100, 40)

current_mode = "line"
drawing = False
start_pos = None
shapes = []  # simpan semua bentuk yang sudah digambar

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Klik tombol mode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_line.collidepoint(event.pos):
                current_mode = "line"
            elif btn_rect.collidepoint(event.pos):
                current_mode = "rect"
            elif btn_circle.collidepoint(event.pos):
                current_mode = "circle"
            else:
                # Klik di area gambar
                drawing = True
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and drawing:
            end_pos = event.pos
            shapes.append((current_mode, start_pos, end_pos))
            drawing = False

    # Gambar latar & tombol
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, btn_line, border_radius=10)
    pygame.draw.rect(screen, GREEN, btn_rect, border_radius=10)
    pygame.draw.rect(screen, RED, btn_circle, border_radius=10)

    screen.blit(font.render("Line", True, WHITE), (btn_line.x+20, btn_line.y+5))
    screen.blit(font.render("Rect", True, WHITE), (btn_rect.x+20, btn_rect.y+5))
    screen.blit(font.render("Circle", True, WHITE), (btn_circle.x+10, btn_circle.y+5))

    # Gambar semua bentuk yang sudah disimpan
    for shape, start, end in shapes:
        if shape == "line":
            pygame.draw.line(screen, BLACK, start, end, 2)
        elif shape == "rect":
            x, y = start
            w, h = end[0] - x, end[1] - y
            pygame.draw.rect(screen, BLACK, (x, y, w, h), 2)
        elif shape == "circle":
            center = start
            radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
            pygame.draw.circle(screen, BLACK, center, radius, 2)

    # Preview saat drag
    if drawing and start_pos:
        current_pos = pygame.mouse.get_pos()
        if current_mode == "line":
            pygame.draw.line(screen, GRAY, start_pos, current_pos, 2)
        elif current_mode == "rect":
            x, y = start_pos
            w, h = current_pos[0]-x, current_pos[1]-y
            pygame.draw.rect(screen, GRAY, (x, y, w, h), 2)
        elif current_mode == "circle":
            center = start_pos
            radius = int(((current_pos[0]-center[0])**2 + (current_pos[1]-center[1])**2)**0.5)
            pygame.draw.circle(screen, GRAY, center, radius, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()