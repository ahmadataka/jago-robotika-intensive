import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Week 4 - Quiz Multi Pertanyaan")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# List soal
questions = [
    {"q": "Ibukota Indonesia?", "a": ["Jakarta", "Bandung", "Medan"], "c": 0},
    {"q": "2+2=?", "a": ["3", "4", "5"], "c": 1},
    {"q": "Warna bendera Indonesia?", "a": ["Merah Putih", "Biru Putih", "Hijau Kuning"], "c": 0},
]

current_q = 0
score = 0
message = ""
show_next = False

def make_buttons(options):
    buttons = []
    for i, text in enumerate(options):
        rect = pygame.Rect(200, 200 + i*80, 400, 60)
        buttons.append((rect, text, i))
    return buttons

buttons = make_buttons(questions[current_q]["a"])
btn_next = pygame.Rect(600, 500, 150, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            if not show_next:
                # Cek jawaban
                for rect, text, idx in buttons:
                    if rect.collidepoint(pos):
                        if idx == questions[current_q]["c"]:
                            message = "Benar!"
                            score += 1
                        else:
                            message = "Salah!"
                        show_next = True
            else:
                # Klik tombol Next
                if btn_next.collidepoint(pos):
                    current_q += 1
                    if current_q < len(questions):
                        buttons = make_buttons(questions[current_q]["a"])
                        message = ""
                        show_next = False
                    else:
                        message = f"Kuis selesai! Skor kamu: {score}/{len(questions)}"

    screen.fill((240, 240, 240))

    if current_q < len(questions):
        qtext = font.render(questions[current_q]["q"], True, (0,0,0))
        screen.blit(qtext, (100, 100))

        for rect, text, idx in buttons:
            pygame.draw.rect(screen, (100,150,250), rect, border_radius=10)
            label = font.render(text, True, (255,255,255))
            screen.blit(label, label.get_rect(center=rect.center))

        if message:
            msg = font.render(message, True, (0,100,0))
            screen.blit(msg, (100, 450))

        if show_next:
            pygame.draw.rect(screen, (200,80,80), btn_next, border_radius=10)
            next_label = font.render("Next", True, (255,255,255))
            screen.blit(next_label, next_label.get_rect(center=btn_next.center))
    else:
        # Skor akhir
        final = font.render(message, True, (0,0,0))
        screen.blit(final, (200, 250))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
