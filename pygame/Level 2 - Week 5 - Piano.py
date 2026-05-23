import pygame
pygame.init()

# Setup window
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 5 - Virtual Piano (Simple)")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Load sounds
sound_c = pygame.mixer.Sound("note_C4.wav")
sound_d = pygame.mixer.Sound("note_D4.wav")
sound_e = pygame.mixer.Sound("note_E4.wav")

# Define rectangles for keys
key_a = pygame.Rect(50, 100, 100, 150)
key_s = pygame.Rect(200, 100, 100, 150)
key_d = pygame.Rect(350, 100, 100, 150)

# State: is the key pressed?
a_pressed = False
s_pressed = False
d_pressed = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                sound_c.play()
                a_pressed = True
            if event.key == pygame.K_s:
                sound_d.play()
                s_pressed = True
            if event.key == pygame.K_d:
                sound_e.play()
                d_pressed = True

        # If a key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a_pressed = False
            if event.key == pygame.K_s:
                s_pressed = False
            if event.key == pygame.K_d:
                d_pressed = False

    # Draw background
    screen.fill((240, 240, 240))

    # Draw keys
    color_a = (200,100,100) if a_pressed else (255,255,255)
    color_s = (200,100,100) if s_pressed else (255,255,255)
    color_d = (200,100,100) if d_pressed else (255,255,255)

    pygame.draw.rect(screen, color_a, key_a)
    pygame.draw.rect(screen, (0,0,0), key_a, 2)
    screen.blit(font.render("A", True, (0,0,0)), key_a.move(40, 60))

    pygame.draw.rect(screen, color_s, key_s)
    pygame.draw.rect(screen, (0,0,0), key_s, 2)
    screen.blit(font.render("S", True, (0,0,0)), key_s.move(40, 60))

    pygame.draw.rect(screen, color_d, key_d)
    pygame.draw.rect(screen, (0,0,0), key_d, 2)
    screen.blit(font.render("D", True, (0,0,0)), key_d.move(40, 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()