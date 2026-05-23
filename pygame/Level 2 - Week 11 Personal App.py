import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 12 - About Me App")

font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (80, 130, 255)
GREEN = (60, 180, 60)
RED = (200, 60, 60)

# Load image & music (replace with your own files)
profile_img = pygame.image.load("player.png")  # student photo or avatar
profile_img = pygame.transform.scale(profile_img, (200, 200))
pygame.mixer.music.load("win.mp3")  # favorite song

# Buttons
btn_profile = pygame.Rect(100, 400, 120, 50)
btn_hobby = pygame.Rect(280, 400, 120, 50)
btn_music = pygame.Rect(460, 400, 120, 50)

page = "profile"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_profile.collidepoint(event.pos):
                page = "profile"
            elif btn_hobby.collidepoint(event.pos):
                page = "hobby"
            elif btn_music.collidepoint(event.pos):
                page = "music"
                pygame.mixer.music.play()

    screen.fill(WHITE)

    # Content
    if page == "profile":
        screen.blit(profile_img, (250, 100))
        text = font.render("Hello, I'm [Name]!", True, BLACK)
        screen.blit(text, (180, 50))
        screen.blit(small_font.render("I love coding and robotics.", True, BLACK), (180, 320))

    elif page == "hobby":
        screen.blit(font.render("My Hobbies:", True, BLACK), (230, 80))
        hobbies = ["🎮 Gaming", "🤖 Robotics", "🎨 Drawing", "📚 Reading"]
        for i, h in enumerate(hobbies):
            screen.blit(small_font.render(h, True, BLACK), (260, 150 + 40*i))

    elif page == "music":
        screen.blit(font.render("My Favorite Song 🎵", True, BLACK), (200, 150))
        screen.blit(small_font.render("Playing music.mp3 ...", True, BLACK), (220, 220))

    # Buttons
    pygame.draw.rect(screen, BLUE, btn_profile, border_radius=15)
    pygame.draw.rect(screen, GREEN, btn_hobby, border_radius=15)
    pygame.draw.rect(screen, RED, btn_music, border_radius=15)

    screen.blit(small_font.render("Profile", True, WHITE), btn_profile.move(25, 10))
    screen.blit(small_font.render("Hobby", True, WHITE), btn_hobby.move(30, 10))
    screen.blit(small_font.render("Music", True, WHITE), btn_music.move(35, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()