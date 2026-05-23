import pygame
pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 8 - Calculator App")
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (180,180,180)
BLUE = (80,130,255)
RED = (200,60,60)

# Layout tombol
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['C']
]

button_rects = []
for row_i, row in enumerate(buttons):
    for col_i, label in enumerate(row):
        x = 60 + col_i*80
        y = 200 + row_i*80
        w, h = 70, 70
        rect = pygame.Rect(x, y, w, h)
        button_rects.append((rect, label))

# Variabel tampilan
expression = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for rect, label in button_rects:
                if rect.collidepoint(event.pos):
                    if label == "C":
                        expression = ""
                    elif label == "=":
                        try:
                            expression = str(eval(expression))
                        except:
                            expression = "Error"
                    else:
                        expression += label

    # Tampilan layar
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (40, 60, 320, 80), border_radius=10)
    text_surface = font.render(expression, True, BLACK)
    screen.blit(text_surface, (50, 80))

    # Gambar tombol
    for rect, label in button_rects:
        color = BLUE if label in "+-*/=" else GRAY
        if label == "C": color = RED
        pygame.draw.rect(screen, color, rect, border_radius=15)
        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=15)
        label_surface = small_font.render(label, True, WHITE)
        screen.blit(label_surface, label_surface.get_rect(center=rect.center))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()