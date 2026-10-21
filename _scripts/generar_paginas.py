"""Genera las páginas internas de Leandro Sauchella (comparten head, header, menú y footer).
Volver a correr tras cambios de estructura; el CSS va en styles.css. El index está hecho a mano."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(D)

FONTS = "https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Inter+Tight:wght@300;400;500;600&display=swap"
NAV = [("Perfil", "perfil.html"), ("Intervención en juicio", "intervencion-en-juicio.html"),
       ("Preguntas", "preguntas-frecuentes.html"), ("Contacto", "index.html#contacto")]
CUR = ' aria-current="page"'
GOOGLE = "https://www.google.com/search?q=Leandro+Sauchella+-+Abogado+Penalista&amp;kgmid=/g/11y3mgbf1h#lrd=0x95bccb096176a717:0x6cd0f5e35835fc1b,1,,,,"  # abre el panel de reseñas
GOOGLE_MAPS = "https://maps.google.com/?cid=7841037308038347803"  # ficha de Google Business en Maps
WA_MSG = "Hola, quisiera consultar por una causa penal en etapa de juicio oral."

def head(title, desc, ld=None, robots=None):
    rb = f'<meta name="robots" content="{robots}">\n' if robots else ""
    ldh = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + "\n</script>\n" if ld else ""
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="only light">
<title>{title}</title>
<meta name="description" content="{desc}">
{rb}<meta name="theme-color" content="#0E0D0C">
<link rel="icon" type="image/png" href="./favicon.png">
<link rel="apple-touch-icon" href="./favicon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="Leandro Sauchella">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="./og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.46.0/dist/tabler-icons.min.css">
<link rel="stylesheet" href="./styles.css">
{ldh}</head>
<body>
'''

def header(active=None):
    links = "\n".join(f'      <a href="./{h}"{CUR if h == active else ""}>{t}</a>' for t, h in NAV)
    return f'''
<!-- ============ HEADER ============ -->
<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    <a href="./index.html" class="brand" aria-label="Leandro Sauchella, inicio">
      <picture>
        <source media="(max-width:768px)" srcset="./logo-apilado-claro.png" width="526" height="219">
        <img src="./logo-claro.png" alt="Leandro Sauchella" width="842" height="262">
      </picture>
    </a>
    <nav class="nav" aria-label="Principal">
{links}
    </nav>
    <a class="btn btn-bronze btn-sm hdr-cta" href="./index.html#contacto">Enviar una consulta</a>
    <button class="burger" id="burger" aria-label="Abrir menú" aria-controls="mnav" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>

<div class="mnav-ov" id="mnavOv"></div>
<nav class="mnav" id="mnav" aria-label="Menú">
  <img src="./logo-apilado-claro.png" alt="" class="mnav-logo" width="526" height="219">
{links.replace("      <a", "  <a")}
  <a class="btn btn-bronze" href="./index.html#contacto">Enviar una consulta</a>
</nav>
'''

FOOTER = f'''
<!-- ============ FOOTER ============ -->
<footer class="ftr" id="ftr">
  <div class="wrap ftr-in">
    <div class="ftr-brand">
      <picture>
        <source media="(max-width:768px)" srcset="./logo-apilado-claro.png" width="526" height="219">
        <img src="./logo-claro.png" alt="Leandro Sauchella" width="842" height="262" loading="lazy">
      </picture>
      <p>Abogado penalista. Intervención en juicio oral. Casos seleccionados, actuación personal.</p>
    </div>
    <div class="ftr-col">
      <h4>Navegación</h4>
      <ul>
        <li><a href="./perfil.html">Perfil profesional</a></li>
        <li><a href="./intervencion-en-juicio.html">Intervención en juicio</a></li>
        <li><a href="./preguntas-frecuentes.html">Preguntas frecuentes</a></li>
        <li><a href="./index.html#contacto">Contacto</a></li>
      </ul>
    </div>
    <div class="ftr-col">
      <h4>Contacto</h4>
      <ul class="ftr-data">
        <li><i class="ti ti-map-pin"></i><span>Paraná 426, piso 1, CABA</span></li>
        <li><i class="ti ti-brand-whatsapp"></i><a class="js-wa" href="#" data-msg="{WA_MSG}">WhatsApp</a></li>
        <li><i class="ti ti-brand-google"></i><a href="{GOOGLE_MAPS}" target="_blank" rel="noopener">Perfil oficial de Google Business</a></li>
        <li><i class="ti ti-mail"></i><a href="mailto:info@leandrosauchella.com.ar">info@leandrosauchella.com.ar</a></li>
      </ul>
    </div>
    <div class="ftr-col">
      <h4>Redes</h4>
      <ul class="ftr-social">
        <li><a href="https://www.instagram.com/drleandrosauchella/" target="_blank" rel="noopener" aria-label="Instagram"><i class="ti ti-brand-instagram"></i></a></li>
        <li><a href="https://www.linkedin.com/in/leandro-sauchella-8b0bb56a" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="ti ti-brand-linkedin"></i></a></li>
        <li><a href="https://www.tiktok.com/@drleandrosauchella" target="_blank" rel="noopener" aria-label="TikTok"><i class="ti ti-brand-tiktok"></i></a></li>
      </ul>
    </div>
  </div>
  <div class="ftr-bottom">
    <p>© <span id="yr">2026</span> Leandro Sauchella. Todos los derechos reservados.</p>
    <p><a href="./privacidad.html">Política de privacidad</a></p>
    <p>Desarrollado por <a href="https://www.instagram.com/sageedev/" target="_blank" rel="noopener">@sageeDev</a></p>
  </div>
</footer>

<script src="./main.js"></script>
</body>
</html>
'''

def ph(img, pos, crumb, h1, lead, short=False, extra=""):
    leadh = f'<p class="lead rise d2">{lead}</p>' if lead else ""
    bg = f'  <div class="ph-bg" aria-hidden="true" style="background-image:url(\'./img/{img}.jpg\');background-position:{pos}"></div>\n' if img else ""
    return f'''
<!-- ============ CABECERA ============ -->
<section class="ph{' ph-short' if short else ''}">
{bg}  <div class="wrap ph-in">
    <nav aria-label="Ruta"><ol class="crumbs"><li><a href="./index.html">Inicio</a></li><li><i class="ti ti-chevron-right" aria-hidden="true"></i><span aria-current="page">{crumb}</span></li></ol></nav>
    <h1 class="ph-h1 split-words">{h1[0]} <em>{h1[1]}</em></h1>
    {leadh}{extra}
  </div>
</section>
'''

def cta(h2, lead):
    return f'''
<!-- ============ CIERRE ============ -->
<section class="cta-band">
  <div class="wrap reveal">
    <h2 class="h2">{h2[0]} <em>{h2[1]}</em></h2>
    <p class="lead">{lead}</p>
    <div class="cta-ctas">
      <a class="btn btn-bronze" href="./index.html#contacto">Enviar una consulta</a>
      <a class="btn btn-wa js-wa" href="#" data-msg="{WA_MSG}">Escribir por WhatsApp</a>
    </div>
  </div>
</section>
'''

def page(name, html):
    open(name, "w", encoding="utf8", newline="\n").write(html)
    print("ok", name)

PROCESO = '''    <div class="proceso" id="proceso">
      <ol class="pr-steps">
        <li><span class="pr-n">01</span><h3>Elevación a juicio</h3><p>Radicación de la causa ante el Tribunal Oral.</p></li>
        <li><span class="pr-n">02</span><h3>Preparación</h3><p>Auditoría del expediente, ofrecimiento de prueba, testigos, peritos y teoría del caso.</p></li>
        <li><span class="pr-n">03</span><h3>Juicio oral y público</h3><p>Litigación en audiencias, examen de testigos y alegatos.</p></li>
        <li><span class="pr-n">04</span><h3>Veredicto y sentencia</h3><p>Asistencia técnica recursiva (Recurso de Casación) hasta la resolución definitiva de la causa.</p></li>
      </ol>
      <div class="pr-track" aria-hidden="true"><span class="pr-fill"></span><em>Mi intervención</em></div>
    </div>'''

# ================================================================== PERFIL
perfil = head("Perfil profesional | Leandro Sauchella, abogado penalista",
  "Abogado penalista (UBA). En la práctica judicial desde 1994 y, desde 2010, con un estudio dedicado exclusivamente a la etapa de juicio oral.",
  {"@context": "https://schema.org", "@type": "Person", "name": "Leandro Sauchella", "jobTitle": "Abogado penalista",
   "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidad de Buenos Aires"},
   "sameAs": ["https://www.instagram.com/drleandrosauchella/", "https://www.linkedin.com/in/leandro-sauchella-8b0bb56a", "https://www.tiktok.com/@drleandrosauchella"]}
  ) + header("perfil.html") + "\n<main>\n" + ph("escalera", "center 40%", "Perfil profesional", ("Leandro Sauchella", "Abogado penalista."), "", extra=f'''
    <ul class="ph-list rise d2">
      <li>Egresado de la Universidad de Buenos Aires.</li>
      <li>Más de 25 años de experiencia en el fuero penal.</li>
      <li>Desde 2010, dedicación exclusiva a la actuación ante Tribunales de Juicio Oral.</li>
    </ul>
    <div class="g-rating rise d3">
      <span class="g-stars" role="img" aria-label="5 de 5 estrellas">★★★★★</span>
      <p><b>5.0 en Google</b> <small>(138 opiniones de clientes)</small></p>
      <a class="btn btn-line btn-sm" href="{GOOGLE}" target="_blank" rel="noopener"><i class="ti ti-brand-google"></i>Ver reseñas</a>
    </div>''') + '''
<!-- ============ BIOGRAFÍA ============ -->
<section class="bio">
  <div class="wrap perfil-grid">
    <figure class="perfil-foto">
      <img src="./img/retrato.jpg" alt="Leandro Sauchella en su estudio" width="1600" height="1787">
    </figure>
    <div class="perfil-copy reveal">
      <p class="eyebrow">Trayectoria</p>
      <h2 class="h2">Un recorrido <em>hacia el juicio oral.</em></h2>
      <p class="lead">Soy abogado, egresado de la Universidad de Buenos Aires, con práctica en Derecho Penal.</p>
      <p>Desde 1994 trabajé en distintos estudios jurídicos, participando en la atención de conflictos diversos y en la dinámica cotidiana del trabajo ante tribunales. Ese recorrido me permitió adquirir una experiencia sostenida en la práctica judicial y, con el tiempo, orientar mi actividad de manera específica hacia la etapa de juicio.</p>
      <p>En 2010 inicié mi estudio jurídico con una orientación exclusiva hacia esa etapa del proceso. Desde entonces concentro mi trabajo en la preparación del caso para el debate y en la actuación directa en audiencia.</p>
    </div>
  </div>
</section>
''' + open("_scripts/resenas.html", encoding="utf8").read() + '''
<!-- ============ LÍNEA DE TIEMPO ============ -->
<section class="hitos-sec">
  <div class="wrap">
    <ol class="tl-h">
      <li class="reveal"><b>1994</b><h3>Práctica judicial</h3><p>Trabajo en distintos estudios jurídicos y en la dinámica diaria ante tribunales.</p></li>
      <li class="reveal"><b>Con el tiempo</b><h3>Foco en el juicio</h3><p>La experiencia acumulada orienta la actividad hacia la etapa de juicio.</p></li>
      <li class="reveal"><b>2010</b><h3>Estudio propio</h3><p>Con orientación exclusiva hacia la etapa de juicio oral.</p></li>
      <li class="reveal"><b>Hoy</b><h3>Actuación personal</h3><p>Preparación del caso y actuación directa en audiencia, en casos seleccionados.</p></li>
    </ol>
  </div>
</section>

<!-- ============ PRINCIPIOS ============ -->
<section class="principios">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Líneas de trabajo</p>
      <h2 class="h2">Una forma de trabajo <em>sin atajos.</em></h2>
    </div>
    <ul class="princ-list">
      <li class="reveal"><span class="m-n">I</span><h3>Exclusividad</h3><p>No desarrollo una práctica generalista: concentro mi trabajo en el juicio oral.</p></li>
      <li class="reveal"><span class="m-n">II</span><h3>Actuación personal</h3><p>No delego la intervención en juicio. Preparo y llevo cada audiencia personalmente.</p></li>
      <li class="reveal"><span class="m-n">III</span><h3>Casos seleccionados</h3><p>Tomo los casos a los que puedo dedicar el estudio y la preparación que el debate exige.</p></li>
      <li class="reveal"><span class="m-n">IV</span><h3>Recurso de Casación</h3><p>Litigación y fundamentación del Recurso de Casación ante Tribunales Superiores.</p></li>
    </ul>
  </div>
</section>
''' + cta(("¿Tu causa está", "en etapa de juicio?"), "Cada consulta se lee personalmente y se evalúa según la instancia del caso y su complejidad.") + "\n</main>\n" + FOOTER
page("perfil.html", perfil)

# ================================================================== INTERVENCIÓN EN JUICIO
BLOQUES = [
 ("I", "Preparación del juicio", "El juicio no comienza el día de la audiencia.", [
   "Comienza mucho antes, con el análisis del expediente y la confección de la teoría del caso, entendida como la definición clara de los hechos que serán llevados a debate, la prueba que los sustenta y la forma en que serán expuestos en audiencia.",
   "Esa preparación organiza el sentido del juicio, orienta la producción de la prueba y condiciona el desarrollo del debate ante el tribunal.",
   "Cuando el caso lo requiere, trabajo con peritos y consultores especializados, integrados a la estrategia del caso y al enfoque del debate."]),
 ("II", "Audiencia de juicio", "No es una instancia de improvisación ni de apuesta.", [
   "La audiencia es el espacio donde el caso se desarrolla públicamente y donde se pone a prueba todo el trabajo previo.",
   "Al juicio se llega con un escenario analizado, con hipótesis de resultado reales y con una planificación construida con meses de anticipación.",
   "La intervención en la sala exige un control estricto del ritmo del debate, conducción técnica del examen y contraexamen de testigos y peritos, lectura permanente del tribunal y capacidad de respuesta inmediata frente a lo que ocurre en sala. Mi actuación en esta etapa es personal y directa, con presencia constante en audiencia y conducción integral del caso hasta su definición."]),
 ("III", "Presencia personal y casos seleccionados", "No delego la intervención en juicio.", [
   "La preparación técnica del caso y la actuación directa en la audiencia de debate son parte de una misma responsabilidad que asumo de manera estrictamente personal.",
   "Este modo de conducción —orientado a la atención de casos seleccionados en CABA y Provincia de Buenos Aires— exige tiempo exclusivo, estudio dogmático y una preparación cuidadosa, muchas veces artesanal, indispensable para litigar en los estrados."]),
]
bloques = "\n".join(f'''    <article class="bloque reveal">
      <div class="bloque-head"><span class="m-n">{n}</span><h2>{t}</h2></div>
      <div class="bloque-body">
        <p class="bloque-key">{k}</p>
{chr(10).join(f"        <p>{p}</p>" for p in ps)}
      </div>
    </article>''' for n, t, k, ps in BLOQUES)
interv = head("Intervención en juicio oral | Leandro Sauchella, abogado penalista",
  "Preparación del juicio, actuación en audiencia y presencia personal: cómo intervengo en la etapa de juicio oral penal, desde la elevación hasta la sentencia.") + header("intervencion-en-juicio.html") + "\n<main>\n" + ph(
  "columnas", "center 40%", "Intervención en juicio", ("Intervención en juicio oral,", "de principio a fin."),
  "Preparo cada caso para el debate y actúo personalmente en la audiencia, hasta la sentencia.") + f'''
<!-- ============ PROCESO ============ -->
<section class="etapa">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Mi intervención</p>
      <h2 class="h2">Desde la elevación <em>hasta la sentencia.</em></h2>
    </div>
{PROCESO}
  </div>
</section>

<!-- ============ TRES PILARES ============ -->
<section class="bloques">
  <div class="wrap">
{bloques}
  </div>
</section>

''' + cta(("Contame en qué instancia", "está la causa."), "Las consultas se evalúan según la instancia del caso y su complejidad; en función de eso defino la posibilidad de una entrevista.") + "\n</main>\n" + FOOTER
page("intervencion-en-juicio.html", interv)

# ================================================================== PREGUNTAS FRECUENTES
FAQ_BLOQUES = [
 ("En la etapa de instrucción", "La investigación penal", [
  ("¿Estoy obligado a declarar en la indagatoria?",
   "<p>No. La ley procesal y la Constitución Nacional garantizan que el silencio no puede tomarse como presunción en contra. Sin embargo, el riesgo real es el inverso: una declaración improvisada, prestada sin conocer la prueba de cargo, condiciona y encadena la defensa penal en el juicio oral que se celebrará años después.</p><p>La indagatoria es el desayuno del proceso; no se puede cenar sin pagar el costo de lo que se eligió a la mañana.</p>"),
  ("¿Se lee en el juicio oral lo que declaré en la investigación escrita?",
   "<p>Sí, se puede leer legítimamente. El artículo 378 del Código Procesal Penal de la Nación habilita la lectura de tus actas de instrucción si decidís no declarar en el debate o si incurrís en contradicciones. Como la mayoría de los imputados prefiere el silencio al inicio del debate, este supuesto ocurre con mucha frecuencia en los tribunales técnicos. Por eso, una mala declaración inicial te obliga a abrir el juicio en una postura puramente defensiva y de alto riesgo.</p>"),
  ("¿Qué pasa si mi abogado anterior omitió pruebas o peritajes durante la instrucción?",
   "<p>Los errores de la investigación penal viajan con el expediente hasta el tribunal oral. Testigos que no se citaron, registros telefónicos no requeridos, videos no aportados o peritajes oficiales desarrollados sin el control de un perito de parte (art. 259 CPPN) debilitan el caso y el margen de maniobra en el debate se estrecha.</p><p>Sin embargo, un abogado dedicado al juicio oral sabe auditar el expediente foja por foja para reparar y mitigar el impacto mediante herramientas procesales clave:</p><ul><li><b>Instrucción suplementaria (art. 357 CPPN):</b> para solicitar aquellas medidas urgentes e indispensables que fueron omitidas en la etapa previa.</li><li><b>Proponer testigos nuevos o peritos:</b> introducir al debate testimonios o expertos que no hayan sido aportados oportunamente, fundamentando rigurosamente ante el Tribunal las razones de su relevancia.</li><li><b>Suspensión del debate:</b> solicitar la interrupción de las audiencias o la fijación de una nueva fecha de juicio cuando la aparición de una prueba novedosa o un imprevisto procesal exija readecuar la estrategia para resguardar las garantías constitucionales.</li><li><b>Contraexamen:</b> maximizar el uso de las técnicas de litigación oral en la audiencia para exponer las contradicciones de los testigos y las debilidades de la investigación previa.</li></ul>"),
 ]),
 ("Cuando terminó la instrucción", "Hacia el juicio oral", [
  ("¿Se puede cambiar de abogado defensor o querellante si la causa ya fue elevada a juicio?",
   "<p>Sí, la sustitución técnica es un derecho inalienable en cualquier instancia. La <b>elevación a juicio oral</b> es el momento exacto para evaluar de forma realista si la estrategia previa es apta para el litigio en estrado.</p><p>El juicio no se improvisa; exige una preparación exclusiva centrada en la teoría del caso: definir qué se quiere obtener y qué pruebas lo respaldan. Una representación penal que solo reacciona ante la acusación fiscal difícilmente convence al tribunal.</p>"),
  ("¿Conviene siempre ir a debate o existen alternativas previas al juicio oral?",
   "<p>Ir a un juicio oral es una decisión estratégica, no un acto de fe. Implica concentrar el máximo nivel de riesgo porque el resultado queda a criterio absoluto del tribunal. Dependiendo del delito y la jurisdicción (CABA o PBA), existen salidas alternativas que una defensa responsable debe evaluar a tiempo:</p><ul><li><b>Juicio abreviado (art. 431 bis CPPN):</b> acuerdo de pena con la fiscalía evitando el debate completo.</li><li><b>Suspensión del juicio a prueba (art. 76 bis CP):</b> extinción de la acción penal bajo reglas de conducta.</li><li><b>Reparación integral y conciliación (art. 59 inc. 6 CP):</b> acuerdos con la víctima que cierran la causa.</li></ul>"),
  ("¿Tengo que declarar en el juicio oral?",
   "<p><b>Si sos el imputado: no estás obligado a declarar.</b> La decisión de cuándo declarar, cómo hacerlo y en qué momento preciso del debate es estrictamente estratégica y la define tu abogado defensor. Como imputado, tenés el derecho constitucional a prestar declaración en cualquier momento de las audiencias, todas las veces que sea necesario antes del cierre del debate, o bien ejercer tu derecho al silencio sin que esto genere ninguna presunción en tu contra. Un litigante experimentado evaluará el impacto de las pruebas de cargo antes de aconsejarte el momento exacto para dirigirte al Tribunal.</p><p><b>Si sos la víctima: sí, por regla general tenés la obligación legal de declarar en el juicio oral</b> en calidad de testigo esencial de los hechos. Sin embargo, <b>el abogado debe planificar estratégicamente el orden en que ese testimonio será vertido en el debate</b>. La determinación del momento oportuno para que la víctima preste su declaración depende de manera directa de las particularidades de la causa, de la naturaleza de los hechos y del orden en que deban introducirse los demás testigos y peritos para consolidar la acusación penal ante el Tribunal.</p>"),
 ]),
]
FAQ = [qa for _, _, qs in FAQ_BLOQUES for qa in qs]
import re as _re
plain = lambda h: _re.sub(r"\s+", " ", _re.sub(r"<[^>]+>", " ", h)).replace(" :", ":").strip()
li = lambda q, a: f'      <li><details><summary><span>{q}</span><i class="ti ti-plus" aria-hidden="true"></i></summary><div class="faq-a">{a}</div></details></li>'
blk = lambda t, sub, qs: '    <div class="faq-block reveal">\n      <h2 class="faq-bt">' + t + ' <em>' + sub + '</em></h2>\n      <ul class="faq-list">\n' + "\n".join(li(q, a) for q, a in qs) + '\n      </ul>\n    </div>'
items = "\n".join(blk(t, sub, qs) for t, sub, qs in FAQ_BLOQUES)
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in FAQ]}
pf = head("Preguntas frecuentes | De la instrucción al juicio oral · Leandro Sauchella",
  "¿Estoy obligado a declarar en la indagatoria? ¿Se puede cambiar de abogado si la causa ya fue elevada a juicio? Respuestas de un abogado penalista dedicado al juicio oral.", faq_ld
  ) + header("preguntas-frecuentes.html") + "\n<main>\n" + ph("palacio", "center 35%", "Preguntas frecuentes", ("De la instrucción", "al juicio oral."),
  "Las dudas más habituales, ordenadas según la etapa en la que está la causa.") + f'''
<!-- ============ PREGUNTAS ============ -->
<section class="faq faq-page">
  <div class="wrap faq-page-in">
{items}
    <p class="faq-note reveal">Esta información tiene finalidad informativa y no constituye asesoramiento legal para un caso concreto. Cada causa depende de sus constancias, de su calificación legal y del código procesal aplicable.</p>
  </div>
</section>
''' + cta(("¿Tenés una causa", "elevada a juicio?"), "Cada consulta se lee personalmente y se evalúa según la instancia del caso.") + "\n</main>\n" + FOOTER
page("preguntas-frecuentes.html", pf)

# ================================================================== PRIVACIDAD
priv = head("Política de privacidad | Leandro Sauchella", "Cómo se tratan los datos personales recibidos a través de este sitio, conforme a la Ley 25.326.") + header() + "\n<main>\n" + ph(
  None, "", "Política de privacidad", ("Política", "de privacidad."), "Cómo se tratan los datos que se envían a través de este sitio.", short=True) + '''
<section class="legal">
  <div class="wrap legal-in">
    <p class="legal-date">Última actualización: octubre de 2026</p>
    <h2>1. Responsable</h2>
    <p>El responsable del tratamiento es Leandro Sauchella, abogado, con domicilio profesional en Paraná 426, piso 1, Ciudad Autónoma de Buenos Aires. Contacto: info@leandrosauchella.com.ar · +54 9 11 5041-9561.</p>
    <h2>2. Qué datos se recopilan</h2>
    <p>Solo los que se envían voluntariamente: nombre y apellido, email, teléfono, la instancia y la jurisdicción de la causa y la descripción que se escribe en el formulario, o los datos que se comparten al escribir por WhatsApp. El sitio no usa cookies de seguimiento ni herramientas de publicidad.</p>
    <h2>3. Para qué se usan</h2>
    <p>Para evaluar la consulta, responderla y, si corresponde, coordinar una entrevista profesional. No se usan para otros fines ni se ceden a terceros con fines comerciales.</p>
    <h2>4. Secreto profesional</h2>
    <p>La información recibida está protegida por el secreto profesional que rige el ejercicio de la abogacía.</p>
    <h2>5. Servicios de terceros</h2>
    <p>Para funcionar, el sitio usa servicios externos que pueden procesar datos técnicos (como la dirección IP):</p>
    <ul>
      <li><b>FormSubmit</b>, que envía al correo del estudio los datos del formulario de contacto.</li>
      <li><b>WhatsApp</b> (Meta Platforms), si se elige escribir por ese medio.</li>
      <li><b>Google Fonts</b> y <b>jsDelivr</b>, que sirven las tipografías y los íconos del sitio.</li>
    </ul>
    <p>Cada uno se rige por su propia política de privacidad.</p>
    <h2>6. Conservación y seguridad</h2>
    <p>Los datos se conservan el tiempo necesario para atender la consulta y cumplir obligaciones legales y profesionales, con medidas razonables de protección.</p>
    <h2>7. Derechos</h2>
    <p>Conforme a la Ley 25.326, el titular de los datos puede solicitar en forma gratuita el acceso, la rectificación, la actualización o la supresión de sus datos, por los medios indicados en el punto 1. La Agencia de Acceso a la Información Pública, órgano de control de la Ley 25.326, atiende las denuncias y los reclamos por incumplimientos de las normas sobre protección de datos personales.</p>
    <h2>8. Cambios</h2>
    <p>Esta política puede actualizarse. La versión vigente es siempre la publicada en esta página.</p>
  </div>
</section>
''' + "\n</main>\n" + FOOTER
page("privacidad.html", priv)

# ================================================================== 404
nf = head("Página no encontrada | Leandro Sauchella", "La página que buscás no existe o cambió de dirección.", robots="noindex") + header() + '''
<main>
<section class="nf">
  <div class="nf-bg" aria-hidden="true"></div>
  <div class="wrap nf-in">
    <span class="nf-num" aria-hidden="true">404</span>
    <h1 class="ph-h1">Esta página <em>no existe.</em></h1>
    <p class="lead">Puede que haya cambiado de dirección. Volvé al inicio o enviá tu consulta.</p>
    <div class="ph-ctas">
      <a class="btn btn-bronze" href="./index.html">Volver al inicio</a>
      <a class="btn btn-line" href="./index.html#contacto">Enviar una consulta</a>
    </div>
  </div>
</section>
</main>
''' + FOOTER
page("404.html", nf)
