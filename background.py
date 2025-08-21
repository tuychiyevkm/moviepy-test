# background.py – fon yaratish funksiyalari
from moviepy.editor import VideoFileClip, ColorClip, ImageClip
import numpy as np
from PIL import Image
import os
import config

def make_gradient_bg(w, h, top=(15, 17, 22), bottom=(0, 0, 0)):
    """Vertikal gradient fon qaytaradi"""
    top = np.array(top, dtype=np.float32)
    bottom = np.array(bottom, dtype=np.float32)
    alpha = np.linspace(0.0, 1.0, h).reshape(h, 1, 1)
    grad = (top * (1 - alpha) + bottom * alpha).astype(np.uint8)
    grad = np.repeat(grad, w, axis=1)
    return Image.fromarray(grad, mode="RGB")

def make_background():
    if config.BG_MODE == "solid":
        return ColorClip(size=(config.W, config.H),
                         color=config.BG_SOLID_COLOR,
                         duration=config.DURATION)

    elif config.BG_MODE == "gradient":
        pil_bg = make_gradient_bg(config.W, config.H,
                                  top=(20, 22, 30), bottom=(5, 6, 8))
        return ImageClip(np.array(pil_bg)).set_duration(config.DURATION)

    elif config.BG_MODE == "video" and config.BG_VIDEO_PATH and os.path.exists(config.BG_VIDEO_PATH):
        bg = VideoFileClip(config.BG_VIDEO_PATH).without_audio()
        bg = bg.resize(height=config.H)
        if bg.w < config.W:
            bg = bg.resize(width=config.W)
        x1 = max(0, (bg.w - config.W) // 2)
        y1 = max(0, (bg.h - config.H) // 2)
        return bg.crop(x1=x1, y1=y1, x2=x1+config.W, y2=y1+config.H).set_duration(config.DURATION)

    else:
        # default gradient
        pil_bg = make_gradient_bg(config.W, config.H,
                                  top=(20, 22, 30), bottom=(5, 6, 8))
        return ImageClip(np.array(pil_bg)).set_duration(config.DURATION)
