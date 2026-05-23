import pygame
pygame.init()

# Setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Ball with Drag and Drop")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (80, 130, 255)

# Ball properties
ball_x = WIDTH // 2
ball_y = 50
ball_radius = 25
velocity = 0
gravity = 0.5
bounce_factor = 0.7
floor = HEIGHT - ball_radius
dragging = False  # flag to know if the ball is being dragged

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse down → start dragging if clicked on the ball
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            distance = ((mx - ball_x) ** 2 + (my - ball_y) ** 2) ** 0.5
            if distance <= ball_radius:
                dragging = True
                velocity = 0  # stop movement while dragging

        # Mouse up → release ball
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dragging = False

        # While dragging, update ball position to mouse position
        elif event.type == pygame.MOUSEMOTION and dragging:
            ball_x, ball_y = event.pos

    # Physics update only if not dragging
    if not dragging:
        velocity += gravity
        ball_y += velocity

        if ball_y >= floor:
            ball_y = floor
            velocity = -velocity * bounce_factor

            if abs(velocity) < 0.5:
                velocity = 0

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # If dragging, show an outline to indicate control
    if dragging:
        pygame.draw.circle(screen, (0, 0, 0), (int(ball_x), int(ball_y)), ball_radius + 3, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()