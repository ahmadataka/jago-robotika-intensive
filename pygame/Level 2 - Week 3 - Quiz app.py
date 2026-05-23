import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 3 - Quiz Interaktif")
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# Soal dan jawaban
question = "Ibukota Indonesia adalah?"
answers = ["Jakarta", "Bandung", "Surabaya"]
correct = 0  # index jawaban benar

# Buat tombol jawaban
buttons = []
for i, text in enumerate(answers):
    rect = pygame.Rect(200, 200 + i*80, 400, 60)
    buttons.append((rect, text))

message = ""
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, (rect, text) in enumerate(buttons):
                if rect.collidepoint(event.pos):
                    if i == correct:
                        message = "Benar!"
                        score += 1
                    else:
                        message = "Salah!"

    screen.fill((240, 240, 240))

    # tampilkan soal
    qtext = font.render(question, True, (0,0,0))
    screen.blit(qtext, (100, 100))

    # tombol jawaban
    for rect, text in buttons:
        pygame.draw.rect(screen, (100, 150, 250), rect, border_radius=10)
        label = font.render(text, True, (255,255,255))
        screen.blit(label, label.get_rect(center=rect.center))

    # hasil jawaban
    if message:
        msg = font.render(message + f" | Skor: {score}", True, (0,100,0))
        screen.blit(msg, (100, 500))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
