"""Favicon: monograma LS (del logo, en hueso) sobre tinta."""
import os
import numpy as np
from PIL import Image
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
l = Image.open(os.path.join(D, "logo-claro.png")).convert("RGBA"); a = np.array(l)[..., 3]
cols = np.where(a.max(0) > 30)[0]
cut = [(cols[i], cols[i + 1]) for i in range(len(cols) - 1) if cols[i + 1] - cols[i] > 12][0]
mono = l.crop((0, 0, cut[0] + 1, l.height)); mono = mono.crop(mono.getbbox())
S = 400
mono = mono.resize((round(mono.width * S / mono.height), S), Image.LANCZOS)
fav = Image.new("RGBA", (512, 512), (0x0E, 0x0D, 0x0C, 255))
fav.alpha_composite(mono, ((512 - mono.width) // 2, (512 - mono.height) // 2))
fav.convert("RGB").save(os.path.join(D, "favicon.png")); print("ok favicon", mono.size)
