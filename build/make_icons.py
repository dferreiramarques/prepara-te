from PIL import Image, ImageDraw, ImageFont

INK = (38, 50, 62)
PAPER = (250, 250, 246)
GRID = (170, 205, 230)
MARGIN = (216, 74, 74)
BLUE = (47, 111, 143)

def draw_icon(size, maskable=False):
    img = Image.new("RGB", (size, size), PAPER)
    d = ImageDraw.Draw(img)
    pad = int(size * 0.14) if maskable else 0
    step = max(4, size // 12)
    for x in range(pad, size - pad, step):
        d.line([(x, pad), (x, size - pad)], fill=GRID, width=max(1, size // 300))
    for y in range(pad, size - pad, step):
        d.line([(pad, y), (size - pad, y)], fill=GRID, width=max(1, size // 300))
    margin_x = pad + int(size * 0.16)
    d.line([(margin_x, pad), (margin_x, size - pad)], fill=MARGIN, width=max(2, size // 60))
    # rounded card
    card_pad = pad + int(size * 0.08)
    d.rounded_rectangle([card_pad, card_pad, size - pad - int(size*0.04), size - pad - int(size*0.04)],
                         radius=size // 12, outline=INK, width=max(2, size // 45), fill=None)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(size * 0.34))
    except Exception:
        font = ImageFont.load_default()
    text = "5"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    d.text(((size - tw)/2 - bbox[0] + size*0.04, (size - th)/2 - bbox[1]), text, font=font, fill=BLUE)
    return img

for size in [192, 512]:
    draw_icon(size).save(f"icons/icon-{size}.png")
draw_icon(512, maskable=True).save("icons/icon-512-maskable.png")
print("icons done")
