import pygame
pygame.init()

# Window & font
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 1 - Tombol Sederhana")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# State aplikasi
bg_color = (25, 25, 30)

# Definisi tombol (pakai Rect)
button_rect = pygame.Rect(300, 250, 200, 60)
button_color = (60, 140, 255)
button_hover = (90, 170, 255)
text_color = (255, 255, 255)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    hovered = button_rect.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Klik kiri mouse → jika di dalam tombol, lakukan aksi
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                # Aksi: ganti warna background (toggle sederhana)
                bg_color = (40, 120, 60) if bg_color != (40, 120, 60) else (25, 25, 30)

    # Gambar UI
    screen.fill(bg_color)

    # Tombol (warna beda saat hover)
    pygame.draw.rect(screen, button_hover if hovered else button_color, button_rect, border_radius=10)

    # Teks tombol
    label = font.render("Ganti Warna", True, text_color)
    screen.blit(label, label.get_rect(center=button_rect.center))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
