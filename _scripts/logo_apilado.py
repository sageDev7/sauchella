"""Logo apilado de Sauchella para mobile: monograma LS arriba (achicado) y el nombre abajo, centrados.
Parte del logo horizontal (logo.png / logo-claro.png) sin tocarlo."""
import os
import numpy as np
from PIL import Image
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONO_H = 150   # alto del monograma respecto de un nombre de 53 px de alto
for src, dst in (("logo-claro.png", "logo-apilado-claro.png"), ("logo.png", "logo-apilado.png")):
    l = Image.open(os.path.join(D, src)).convert("RGBA"); a = np.array(l)[..., 3]
    cols = np.where(a.max(0) > 30)[0]
    cut = [(cols[i], cols[i + 1]) for i in range(len(cols) - 1) if cols[i + 1] - cols[i] > 12][0]
    mono = l.crop((0, 0, cut[0] + 1, l.height)); mono = mono.crop(mono.getbbox())
    name = l.crop((cut[1], 0, l.width, l.height)); name = name.crop(name.getbbox())
    mono = mono.resize((round(mono.width * MONO_H / mono.height), MONO_H), Image.LANCZOS)
    gap = 16
    W = max(mono.width, name.width); H = mono.height + gap + name.height
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.alpha_composite(mono, ((W - mono.width) // 2, 0))
    out.alpha_composite(name, ((W - name.width) // 2, mono.height + gap))
    out.save(os.path.join(D, dst)); print(dst, out.size)
