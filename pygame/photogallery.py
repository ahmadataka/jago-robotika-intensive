import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Photo Viewer App")

font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# --- Folder containing photos ---
photo_folder = "photos"
os.makedirs(photo_folder, exist_ok=True)

# Load all image file names
images = [f for f in os.listdir(photo_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
if not images:
    print("⚠️ No images found in 'photos' folder.")
    running = False
else:
    running = True

index = 0

# --- Buttons ---
btn_prev = pygame.Rect(100, 500, 150, 50)
btn_next = pygame.Rect(550, 500, 150, 50)

def draw_button(rect, text):
    pygame.draw.rect(screen, (60, 60, 60), rect, border_radius=10)
    txt = font.render(text, True, (255, 255, 255))
    screen.blit(txt, (rect.x + 35, rect.y + 10))

def load_image(path):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (600, 400))
    return img

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_prev.collidepoint(event.pos):
                index = (index - 1) % len(images)
            elif btn_next.collidepoint(event.pos):
                index = (index + 1) % len(images)

    screen.fill((20, 20, 20))

    # Display image
    image_path = os.path.join(photo_folder, images[index])
    image = load_image(image_path)
    screen.blit(image, (100, 60))

    # Display filename
    filename_text = font.render(images[index], True, (255, 255, 255))
    screen.blit(filename_text, (WIDTH // 2 - filename_text.get_width() // 2, 480))

    # Draw buttons
    draw_button(btn_prev, "Prev")
    draw_button(btn_next, "Next")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()