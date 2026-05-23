import pygame
pygame.init()

# --- Setup ---
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Mixer with Save Function")
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 60, 60)
GREEN = (60, 180, 60)
BLUE = (80, 130, 255)
GRAY = (180, 180, 180)

# --- Sliders and boxes ---
slider_width, slider_height = 60, 150
slider_x = [150, 320, 490]
slider_y = 280

# color display rectangles
box_left = pygame.Rect(110, 230, 120, 50)   # red color display
box_mid = pygame.Rect(280, 230, 120, 50)    # green color display
box_right = pygame.Rect(450, 230, 120, 50)  # blue color display

# Preview area (#1)
preview_rect = pygame.Rect(280, 40, 140, 140)

# Save button
btn_save = pygame.Rect(280, 440, 140, 40)

# --- Initial RGB values ---
rgb = [128, 128, 128]

def draw_slider(x, color, value, label):
    # Bar background
    pygame.draw.rect(screen, GRAY, (x, slider_y, slider_width, slider_height))
    # Filled portion (scaled by value)
    filled_height = int((value / 255) * slider_height)
    pygame.draw.rect(screen, color, (x, slider_y + (slider_height - filled_height), slider_width, filled_height))
    # Draw arrows
    up_tri = [(x + slider_width//2, slider_y - 30), (x + 20, slider_y - 10), (x + slider_width - 20, slider_y - 10)]
    down_tri = [(x + slider_width//2, slider_y + slider_height + 30),
                (x + 20, slider_y + slider_height + 10),
                (x + slider_width - 20, slider_y + slider_height + 10)]
    pygame.draw.polygon(screen, color, up_tri)
    pygame.draw.polygon(screen, color, down_tri)
    text = font.render(str(label), True, WHITE)
    screen.blit(text, (x + 20, slider_y + 55))

running = True
dragging = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click → check sliders or save
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if btn_save.collidepoint(event.pos):
                # Save only preview area (#1)
                sub_surface = screen.subsurface(preview_rect)
                pygame.image.save(sub_surface, "./hasil/mixed_color.png")
                print("✅ Saved as mixed_color.png")
            for i, x in enumerate(slider_x):
                if x <= mx <= x + slider_width and slider_y <= my <= slider_y + slider_height:
                    dragging = i

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

        elif event.type == pygame.MOUSEMOTION and dragging is not None:
            _, my = event.pos
            my = max(slider_y, min(slider_y + slider_height, my))
            value = int((slider_height - (my - slider_y)) / slider_height * 255)
            rgb[dragging] = value

    # --- Drawing section ---
    screen.fill(BLACK)

    # Preview area (#1)
    pygame.draw.rect(screen, tuple(rgb), preview_rect)
    pygame.draw.rect(screen, WHITE, preview_rect, 3)
    screen.blit(font.render("1", True, WHITE), (preview_rect.x + 60, preview_rect.y + 55))

    # Sliders (#2, #3, #4)
    draw_slider(slider_x[0], RED, rgb[0], 2)
    draw_slider(slider_x[1], GREEN, rgb[1], 3)
    draw_slider(slider_x[2], BLUE, rgb[2], 4)

    # Color bars (#5, #6)
    pygame.draw.rect(screen, GREEN, box_left, border_radius=20)
    pygame.draw.rect(screen, RED, box_right, border_radius=20)
    screen.blit(font.render("5", True, WHITE), (box_left.x + 45, box_left.y + 5))
    screen.blit(font.render("6", True, WHITE), (box_right.x + 45, box_right.y + 5))

    # Save button
    pygame.draw.rect(screen, GRAY, btn_save, border_radius=10)
    save_text = font.render("Save", True, BLACK)
    screen.blit(save_text, (btn_save.x + 40, btn_save.y + 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()