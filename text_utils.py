# text_utils.py – matnni rasmga yozish
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import textwrap
from moviepy.editor import ImageClip
import config

def load_font(size: int):
    try:
        if config.FONT_PATH:
            return ImageFont.truetype(config.FONT_PATH, size=size)
    except Exception:
        pass
    return ImageFont.load_default()

def draw_text_image(text, max_width, font_size, color=(255,255,255), align="center"):
    """Matndan shaffof PNG yasaydi"""
    if not text:
        return None
    font = load_font(font_size)
    wrapped = textwrap.fill(text, width=30)
    dummy_img = Image.new("RGBA", (max_width, 10))
    draw = ImageDraw.Draw(dummy_img)

    lines = wrapped.split("\n")
    line_heights = []
    max_line_w = 0
    for ln in lines:
        bbox = draw.textbbox((0,0), ln, font=font)
        max_line_w = max(max_line_w, bbox[2]-bbox[0])
        line_heights.append(bbox[3]-bbox[1])

    total_h = int(sum(line_heights)*1.15)
    img = Image.new("RGBA", (max_line_w+10, total_h+10), (0,0,0,0))
    d = ImageDraw.Draw(img)

    y=0
    for ln, lh in zip(lines, line_heights):
        bbox = d.textbbox((0,0), ln, font=font)
        lw = bbox[2]-bbox[0]
        x = (img.width-lw)//2 if align=="center" else 0
        d.text((x,y), ln, font=font, fill=color)
        y += int(lh*1.15)

    return img

def image_to_clip(pil_img, duration, pos=("center","center")):
    arr = np.array(pil_img)
    return ImageClip(arr, transparent=True).set_duration(duration).set_position(pos)
