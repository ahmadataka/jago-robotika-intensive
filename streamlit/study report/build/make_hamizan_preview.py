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

    bg = (255, 255, 255)
    chrome = (244, 244, 245)
    border = (228, 229, 233)
    sidebar = (239, 242, 247)
    text_dark = (47, 52, 66)
    text_med = (82, 88, 102)
    text_light = (120, 127, 140)
    accent = (255, 78, 80)
    teal = (128, 172, 179)

    font_small = load_font(16)
    font_body = load_font(18)
    font_body_bold = load_font(18, bold=True)
    font_h1 = load_font(46, bold=True)
    font_sidebar = load_font(22, bold=True)
    font_nav = load_font(19)

    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=bg)
    draw.rectangle((0, 0, WIDTH, 86), fill=chrome)
    draw.line((0, 86, WIDTH, 86), fill=border, width=2)

    rounded_rect(draw, (2, 22, 78, 50), 10, fill=(232, 233, 236), outline=(215, 217, 222))
    draw.text((40, 36), "streamlitApp", font=load_font(14), fill=text_med, anchor="mm")

    rounded_rect(draw, (84, 15, 212, 54), 18, fill=teal)
    draw.text((148, 35), "Jago Robotika", font=font_small, fill=(255, 255, 255), anchor="mm")

    rounded_rect(draw, (222, 16, 278, 52), 16, fill=(248, 248, 249), outline=border)
    draw.text((238, 35), "‹", font=load_font(26), fill=text_light, anchor="mm")
    draw.text((262, 35), "›", font=load_font(26), fill=text_light, anchor="mm")

    rounded_rect(draw, (359, 15, 840, 52), 18, fill=(248, 248, 249), outline=border)
    draw.text((600, 34), "hamizan.streamlit.app", font=font_small, fill=text_med, anchor="mm")

    rounded_rect(draw, (12, 88, 590, 117), 14, fill=(251, 251, 252), outline=(215, 217, 222))
    rounded_rect(draw, (777, 88, 1190, 117), 14, fill=(251, 251, 252), outline=(215, 217, 222))
    draw.rectangle((216, 86, 217, HEIGHT), fill=border)
    draw.rectangle((777, 86, 778, HEIGHT), fill=border)

    draw.rectangle((0, 118, 244, HEIGHT), fill=sidebar)
    draw.text((25, 173), "Navigation", font=font_sidebar, fill=text_dark)
    draw.text((25, 217), "Go to", font=font_body, fill=text_med)

    items = [("Home", True), ("About Me", False), ("Gallery", False), ("Fun Zone", False), ("Contact", False)]
    start_y = 250
    for i, (label, selected) in enumerate(items):
        y = start_y + i * 32
        radio(draw, (32, y), selected=selected)
        draw.text((48, y), label, font=font_nav, fill=text_dark, anchor="lm")

    draw.text((442, 205), "Welcome to my website!", font=font_h1, fill=text_dark)
    draw.text((443, 273), "Hello! this is my first website using Streamlit.", font=font_body_bold, fill=text_med)

    draw.text((1098, 140), "Fork", font=font_small, fill=text_dark)
    draw.text((1141, 140), "GitHub", font=font_small, fill=text_dark)

    draw.ellipse((1126, 772, 1164, 810), fill=(234, 240, 251))
    draw.text((1145, 791), "+", font=load_font(30), fill=(96, 132, 180), anchor="mm")
    rounded_rect(draw, (1168, 754, 1200, 801), 10, fill=(255, 78, 80))
    draw.text((1184, 779), "▾", font=load_font(24), fill="white", anchor="mm")

    img.save("jago-robotika-intensive/streamlit/study report/app-preview-streamlit.jpg", quality=95)


if __name__ == "__main__":
    main()
