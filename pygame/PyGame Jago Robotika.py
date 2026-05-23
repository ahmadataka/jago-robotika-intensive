import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

GRAY = (100, 100, 100)
teks = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = event.unicode
            if event.key == pygame.K_BACKSPACE:
                teks = teks[:-1]
            elif event.key == pygame.K_RETURN:
                teks = teks + "\n"
            else:
                teks = teks + keys
            if(len(teks)%40==0):
                teks = teks + "\n"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if tombol_clear.collidepoint(event.pos):
                teks = ""
            if tombol_save.collidepoint(event.pos):
                with open("catatan.txt", "w") as f:
                    f.write(teks)
        
    screen.fill((0,0,0))

    # Bikin layar
    pygame.draw.rect(screen, GRAY, (100, 60, 600, 440), border_radius=10)
    
    baris = 70
    for line in teks.split("\n"):
        rendered = font.render(line, True, (255, 255, 255))
        screen.blit(rendered, (110, baris))
        baris = baris + 25
    
    # Bikin tombol
    tombol_save = pygame.draw.rect(screen, (100, 100, 200), (100, 520, 270, 50), border_radius=10)
    label = font.render("Save", True, (255, 255, 255))
    text_rect = label.get_rect(center=tombol_save.center)
    screen.blit(label, text_rect)

    tombol_clear = pygame.draw.rect(screen, (200, 100, 100), (430, 520, 270, 50), border_radius=10)
    label = font.render("Clear", True, (255, 255, 255))
    text_rect = label.get_rect(center=tombol_clear.center)
    screen.blit(label, text_rect)

        
    pygame.display.update()

pygame.quit()
