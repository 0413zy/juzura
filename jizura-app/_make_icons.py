# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import os

D = r"C:\Users\pc\Doubao\chats\2026-10-08\new-chat\jizura-app"
BG = (12, 14, 19)
ACC = (58, 214, 196)

# 波形（64 视口坐标）: (18,20)->(32,38)->(46,21)
wave = [(18, 20), (32, 38), (46, 21)]

def draw_icon(size, radius_ratio, wave_scale, stroke, maskable_pad=0.0):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if maskable_pad:
        # 纯背景铺满整幅（maskable 安全区外也需有底色）
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * 0.0), fill=BG)
        pad = size * maskable_pad
        d.rounded_rectangle([pad, pad, size - pad, size - pad], radius=int((size - 2 * pad) * radius_ratio), fill=BG)
    else:
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius_ratio), fill=BG)
    # 波形居中
    s = size / 64.0 * wave_scale
    ox = size / 2
    oy = size / 2
    pts = [(ox + (x - 32) * s, oy + (y - 32) * s) for (x, y) in wave]
    d.line(pts, fill=ACC, width=max(2, int(size * stroke)), joint="curve")
    # 两端圆头
    for p in pts:
        d.ellipse([p[0] - stroke * size / 2, p[1] - stroke * size / 2,
                   p[0] + stroke * size / 2, p[1] + stroke * size / 2], fill=ACC)
    return img

draw_icon(192, 0.22, 0.92, 0.055).save(os.path.join(D, "icon-192.png"))
draw_icon(512, 0.22, 0.92, 0.055).save(os.path.join(D, "icon-512.png"))
draw_icon(512, 0.22, 0.72, 0.05, maskable_pad=0.12).save(os.path.join(D, "icon-maskable.png"))
draw_icon(180, 0.22, 0.92, 0.055).save(os.path.join(D, "apple-touch-icon.png"))
print("icons done")
