import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 2 - Mini Paint Tool")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE  = (50, 50, 200)

bg_color = WHITE
brush_color = BLACK
brush_size = 5

# Tombol warna
btn_red = pygame.Rect(10, 10, 60, 40)
btn_green = pygame.Rect(80, 10, 60, 40)
btn_blue = pygame.Rect(150, 10, 60, 40)

drawing = False  # state: sedang menggambar atau tidak

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # mulai menggambar
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # klik kiri
                pos = event.pos
                # cek tombol warna
                if btn_red.collidepoint(pos):
                    brush_color = RED
                elif btn_green.collidepoint(pos):
                    brush_color = GREEN
                elif btn_blue.collidepoint(pos):
                    brush_color = BLUE
                else:
                    drawing = True  # mulai gambar
        # berhenti menggambar
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        # drag mouse
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.circle(screen, brush_color, event.pos, brush_size)

    # gambar UI (tombol warna)
    pygame.draw.rect(screen, RED, btn_red)
    pygame.draw.rect(screen, GREEN, btn_green)
    pygame.draw.rect(screen, BLUE, btn_blue)
    screen.blit(font.render("RED", True, WHITE), (15, 20))
    screen.blit(font.render("GREEN", True, WHITE), (85, 20))
    screen.blit(font.render("BLUE", True, WHITE), (155, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
