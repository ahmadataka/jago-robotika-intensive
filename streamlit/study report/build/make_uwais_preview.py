from PIL import Image, ImageDraw, ImageFont


WIDTH = 1200
HEIGHT = 801


def load_font(size: int, bold: bool = False):
    candidates = []
    if bold:
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                "/System/Library/Fonts/Supplemental/Helvetica.ttc",
            ]
        )
    else:
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial.ttf",
                "/System/Library/Fonts/Supplemental/Helvetica.ttc",
            ]
        )

    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded_rect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def radio(draw, center, selected=False):
    x, y = center
    draw.ellipse((x - 8, y - 8, x + 8, y + 8), outline=(195, 199, 209), width=2, fill=(245, 247, 250))
    if selected:
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=(255, 78, 80))


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    chrome = (244, 244, 245)
    border = (228, 229, 233)
    sidebar = (239, 242, 247)
    text_dark = (47, 52, 66)
    text_med = (82, 88, 102)
    text_muted = (138, 141, 149)
    text_light = (120, 127, 140)
    teal = (128, 172, 179)

    font_small = load_font(16)
    font_body = load_font(18)
    font_body_bold = load_font(18, bold=True)
    font_h1 = load_font(46, bold=True)
    font_sidebar = load_font(22, bold=True)
    font_nav = load_font(19)
    font_nav_emoji = load_font(21)

    draw.rectangle((0, 0, WIDTH, HEIGHT), fill="white")
    draw.rectangle((0, 0, WIDTH, 86), fill=chrome)
    draw.line((0, 86, WIDTH, 86), fill=border, width=2)

    rounded_rect(draw, (12, 16, 44, 48), 12, fill=(248, 248, 249), outline=border)
    draw.text((28, 32), "☰", font=load_font(20), fill=text_med, anchor="mm")

    rounded_rect(draw, (52, 15, 168, 54), 18, fill=teal)
    draw.text((110, 34), "Jago Robotika", font=font_small, fill=(255, 255, 255), anchor="mm")

    rounded_rect(draw, (178, 16, 234, 52), 16, fill=(248, 248, 249), outline=border)
    draw.text((194, 35), "‹", font=load_font(26), fill=text_light, anchor="mm")
    draw.text((218, 35), "›", font=load_font(26), fill=text_light, anchor="mm")

    rounded_rect(draw, (359, 15, 840, 52), 18, fill=(248, 248, 249), outline=border)
    draw.text((600, 34), "uwais-learning.streamlit.app", font=font_small, fill=text_med, anchor="mm")

    rounded_rect(draw, (12, 88, 590, 117), 14, fill=(251, 251, 252), outline=(215, 217, 222))
    draw.text((290, 103), "My Personal Website · Streamlit", font=font_small, fill=text_med, anchor="mm")
    rounded_rect(draw, (604, 88, 1190, 117), 14, fill=(251, 251, 252), outline=(215, 217, 222))
    draw.text((897, 103), "Uwais Portfolio · Streamlit", font=font_small, fill=text_med, anchor="mm")

    draw.rectangle((0, 118, 244, HEIGHT), fill=sidebar)
    draw.rectangle((244, 118, 245, HEIGHT), fill=border)

    draw.text((25, 202), "Go to", font=font_body, fill=text_dark)

    items = [
        ("Home", True, "🏠"),
        ("About Me", False, "👤"),
        ("Gallery", False, "🖼"),
        ("Fun Zone", False, "🎮"),
        ("Contact", False, "📫"),
    ]
    start_y = 245
    for i, (label, selected, emoji) in enumerate(items):
        y = start_y + i * 32
        radio(draw, (32, y), selected=selected)
        draw.text((48, y), emoji, font=font_nav_emoji, fill=text_dark, anchor="lm")
        draw.text((72, y), label, font=font_nav, fill=text_dark, anchor="lm")

    draw.text((442, 205), "Welcome to My Website!", font=font_h1, fill=text_dark)
    draw.text((1016, 221), "👋", font=load_font(42), anchor="mm")

    draw.text((443, 274), "Hi! My name is", font=font_body, fill=text_dark)
    draw.text((586, 274), "Uwais Ruzali Rustam Aziz", font=font_body_bold, fill=text_dark)
    draw.text((843, 274), "and this is my personal website.", font=font_body, fill=text_dark)
    draw.text((443, 325), "I made this as a school project to share a little bit about myself.", font=font_body, fill=text_dark)
    draw.text((443, 376), "Use the sidebar on the left to explore the different pages! ", font=font_body, fill=text_dark)
    draw.text((931, 376), "😊", font=load_font(22), anchor="lm")

    draw.text((705, 438), "Abu Dhabi - where I live", font=font_body, fill=text_muted, anchor="mm")
    draw.text((848, 438), "🇦🇪", font=load_font(22), anchor="mm")

    draw.text((1098, 140), "Fork", font=font_small, fill=text_dark)
    draw.text((1141, 140), "GitHub", font=font_small, fill=text_dark)

    rounded_rect(draw, (680, 167, 774, 193), 3, fill=(230, 232, 236), outline=(204, 206, 210))
    draw.text((727, 180), "streamlitApp", font=font_small, fill=(87, 89, 94), anchor="mm")

    draw.ellipse((1126, 772, 1164, 810), fill=(234, 240, 251))
    draw.text((1145, 791), "+", font=load_font(30), fill=(96, 132, 180), anchor="mm")
    rounded_rect(draw, (1168, 754, 1200, 801), 10, fill=(255, 78, 80))
    draw.text((1184, 779), "▾", font=load_font(24), fill="white", anchor="mm")

    img.save("jago-robotika-intensive/streamlit/study report/app-preview-uwais.jpg", quality=95)


if __name__ == "__main__":
    main()
