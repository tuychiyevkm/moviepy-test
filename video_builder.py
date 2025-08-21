# video_builder.py – tayyor video qurish
from moviepy.editor import CompositeVideoClip, vfx
import config
import background
import text_utils

def build_video():
    bg = background.make_background()

    if config.KEN_BURNS_STRENGTH > 0:
        bg = bg.fx(
            vfx.resize,
            lambda t: 1.0 + (config.KEN_BURNS_STRENGTH * (t/config.DURATION))
        )

    clips = [bg]

    # Headline
    headline_img = text_utils.draw_text_image(
        config.HEADLINE,
        max_width=config.W - config.SAFE_MARGIN*2,
        font_size=config.HEADLINE_SIZE,
        color=config.TEXT_COLOR,
        align=config.TEXT_ALIGN
    )
    if headline_img:
        head_clip = text_utils.image_to_clip(
            headline_img,
            duration=config.DURATION,
            pos=("center", config.H//2 - 140)
        ).crossfadein(config.FADE_IN).crossfadeout(config.FADE_OUT)
        clips.append(head_clip)

    # Subtext
    if config.SUBTEXT:
        sub_img = text_utils.draw_text_image(
            config.SUBTEXT,
            max_width=config.W - config.SAFE_MARGIN*2,
            font_size=config.SUBTEXT_SIZE,
            color=config.TEXT_COLOR,
            align=config.TEXT_ALIGN
        )
        if sub_img:
            sub_clip = text_utils.image_to_clip(
                sub_img,
                duration=config.DURATION,
                pos=("center", config.H//2 + 120)
            ).crossfadein(config.FADE_IN+0.2).crossfadeout(config.FADE_OUT)
            clips.append(sub_clip)

    final = CompositeVideoClip(clips, size=(config.W, config.H))
    final = final.set_duration(config.DURATION)

    final.write_videofile(
        config.OUTPUT_PATH,
        fps=config.FPS,
        codec="libx264",
        audio=False,
        bitrate=config.BITRATE
    )
    print(f"✅ Tayyor: {config.OUTPUT_PATH}")
