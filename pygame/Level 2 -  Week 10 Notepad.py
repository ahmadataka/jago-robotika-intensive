import pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 10 - Notepad App")
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
BLUE = (80,130,255)
RED = (200,60,60)

# Buttons
btn_save = pygame.Rect(100, 320, 120, 50)
btn_clear = pygame.Rect(380, 320, 120, 50)

text = ""  # text buffer

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]  # delete last char
            elif event.key == pygame.K_RETURN:
                text += "\n"  # new line
            else:
                text += event.unicode  # add typed character

        # Mouse buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_clear.collidepoint(event.pos):
                text = ""
            elif btn_save.collidepoint(event.pos):
                with open("note.txt", "w") as f:
                    f.write(text)
                print("Text saved to note.txt!")

    # Draw UI
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (50, 50, 500, 240), border_radius=10)
    pygame.draw.rect(screen, BLACK, (50, 50, 500, 240), 2, border_radius=10)

    # Render text
    y_offset = 60
    for line in text.split("\n"):
        rendered = small_font.render(line, True, BLACK)
        screen.blit(rendered, (60, y_offset))
        y_offset += 35

    # Buttons
    pygame.draw.rect(screen, BLUE, btn_save, border_radius=10)
    pygame.draw.rect(screen, RED, btn_clear, border_radius=10)
    screen.blit(small_font.render("Save", True, WHITE), btn_save.move(35, 10))
    screen.blit(small_font.render("Clear", True, WHITE), btn_clear.move(30, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()