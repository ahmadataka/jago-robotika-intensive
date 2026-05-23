import pygame
pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save Rectangle to Image")

WHITE = (255, 255, 255)
BLUE = (80, 130, 255)
RED = (200, 60, 60)
clock = pygame.time.Clock()

# Draw something
screen.fill(WHITE)
pygame.draw.rect(screen, BLUE, (50, 50, 150, 100))
pygame.draw.circle(screen, RED, (200, 200), 50)
pygame.display.flip()

# Wait a second so everything appears
pygame.time.wait(1000)

# Define rectangle area to save
rect_area = pygame.Rect(50, 50, 150, 100)

# Copy that area from the screen
sub_surface = screen.subsurface(rect_area)

# Save as image file
pygame.image.save(sub_surface, "saved_rect.png")
print("Rectangle area saved as saved_rect.png")

pygame.quit()