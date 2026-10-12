"""Genera las páginas internas de Leandro Sauchella (comparten head, header, menú y footer).
Volver a correr tras cambios de estructura; el CSS va en styles.css. El index está hecho a mano."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(D)

FONTS = "https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Inter+Tight:wght@300;400;500;600&display=swap"
NAV = [("Perfil", "perfil.html"), ("Intervención en juicio", "intervencion-en-juicio.html"),
       ("Preguntas", "preguntas-frecuentes.html"), ("Contacto", "index.html#contacto")]
CUR = ' aria-current="page"'
WA_MSG = "Hola, quisiera consultar por una causa penal en etapa de juicio oral."

def head(title, desc, ld=None, robots=None):
    rb = f'<meta name="robots" content="{robots}">\n' if robots else ""
    ldh = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + "\n</script>\n" if ld else ""
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
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
      <p>Abogado penalista. Intervención exclusiva en la etapa de juicio oral. Casos seleccionados, actuación personal.</p>
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
        <li><i class="ti ti-phone"></i><a href="tel:+5491150419561">+54 9 11 5041-9561</a></li>
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

def ph(img, pos, crumb, h1, lead, short=False):
    bg = f'  <div class="ph-bg" aria-hidden="true" style="background-image:url(\'./img/{img}.jpg\');background-position:{pos}"></div>\n' if img else ""
    return f'''
<!-- ============ CABECERA ============ -->
<section class="ph{' ph-short' if short else ''}">
{bg}  <div class="wrap ph-in">
    <nav aria-label="Ruta"><ol class="crumbs"><li><a href="./index.html">Inicio</a></li><li><i class="ti ti-chevron-right" aria-hidden="true"></i><span aria-current="page">{crumb}</span></li></ol></nav>
    <h1 class="ph-h1 split-words">{h1[0]} <em>{h1[1]}</em></h1>
    <p class="lead rise d2">{lead}</p>
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
      <a class="btn btn-line js-wa" href="#" data-msg="{WA_MSG}">Escribir por WhatsApp</a>
    </div>
  </div>
</section>
'''

def page(name, html):
    open(name, "w", encoding="utf8", newline="\n").write(html)
    print("ok", name)

PROCESO = '''    <div class="proceso" id="proceso">
      <ol class="pr-steps">
        <li class="pr-off"><span class="pr-n">01</span><h3>Investigación</h3><p>Instrucción y medidas cautelares</p></li>
        <li><span class="pr-n">02</span><h3>Elevación a juicio</h3><p>El caso llega al tribunal oral</p></li>
        <li><span class="pr-n">03</span><h3>Preparación</h3><p>Expediente, prueba y teoría del caso</p></li>
        <li><span class="pr-n">04</span><h3>Audiencia</h3><p>Debate, testigos y alegatos</p></li>
        <li><span class="pr-n">05</span><h3>Sentencia</h3><p>Conducción hasta la definición</p></li>
      </ol>
      <div class="pr-track" aria-hidden="true"><span class="pr-fill"></span><em>Mi intervención</em></div>
    </div>'''

# ================================================================== PERFIL
perfil = head("Perfil profesional | Leandro Sauchella, abogado penalista",
  "Abogado penalista (UBA). En la práctica judicial desde 1994 y, desde 2010, con un estudio dedicado exclusivamente a la etapa de juicio oral.",
  {"@context": "https://schema.org", "@type": "Person", "name": "Leandro Sauchella", "jobTitle": "Abogado penalista",
   "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidad de Buenos Aires"},
   "sameAs": ["https://www.instagram.com/drleandrosauchella/", "https://www.linkedin.com/in/leandro-sauchella-8b0bb56a", "https://www.tiktok.com/@drleandrosauchella"]}
  ) + header("perfil.html") + "\n<main>\n" + ph("escalera", "center 40%", "Perfil profesional", ("Leandro Sauchella,", "abogado penalista."),
  "Egresado de la Universidad de Buenos Aires. Más de 25 años de experiencia en el fuero y, desde 2010, dedicación exclusiva a la etapa de juicio.") + '''
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
      <p class="eyebrow">Cómo entiendo el ejercicio profesional</p>
      <h2 class="h2">Una forma de trabajo <em>sin atajos.</em></h2>
    </div>
    <ul class="princ-list">
      <li class="reveal"><span class="m-n">I</span><h3>Exclusividad</h3><p>No desarrollo una práctica generalista: intervengo solo en la etapa de juicio oral.</p></li>
      <li class="reveal"><span class="m-n">II</span><h3>Actuación personal</h3><p>No delego la intervención en juicio. Preparo y llevo cada audiencia personalmente.</p></li>
      <li class="reveal"><span class="m-n">III</span><h3>Casos seleccionados</h3><p>Tomo los casos a los que puedo dedicar el estudio y la preparación que el debate exige.</p></li>
    </ul>
    <blockquote class="cita cita-c reveal">Trabajo de manera personal y en casos seleccionados. Ese es el modo en que entiendo el ejercicio profesional.</blockquote>
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
   "La intervención exige control del ritmo del debate, conducción del examen y contraexamen de testigos, lectura permanente del tribunal y capacidad de respuesta inmediata frente a lo que ocurre en sala. Mi actuación en esta etapa es personal y directa, con presencia constante en audiencia y conducción integral del caso hasta su definición."]),
 ("III", "Presencia personal", "No delego la intervención en juicio.", [
   "La preparación del caso y la actuación en audiencia son parte de una misma responsabilidad, que asumo de manera personal.",
   "Ese modo de trabajo exige tiempo, estudio y una preparación cuidadosa, muchas veces artesanal."]),
]
bloques = "\n".join(f'''    <article class="bloque reveal">
      <div class="bloque-head"><span class="m-n">{n}</span><h2>{t}</h2></div>
      <div class="bloque-body">
        <p class="bloque-key">{k}</p>
{chr(10).join(f"        <p>{p}</p>" for p in ps)}
      </div>
    </article>''' for n, t, k, ps in BLOQUES)
interv = head("Intervención en juicio oral | Leandro Sauchella, abogado penalista",
  "Preparación del juicio, actuación en audiencia y presencia personal: cómo intervengo en la etapa de juicio oral penal. No tomo causas en etapa de instrucción.") + header("intervencion-en-juicio.html") + "\n<main>\n" + ph(
  "columnas", "center 40%", "Intervención en juicio", ("Intervención en juicio oral,", "de principio a fin."),
  "Preparo cada caso para el debate y actúo personalmente en la audiencia, hasta la sentencia.") + f'''
<!-- ============ PROCESO ============ -->
<section class="etapa">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Una sola etapa del proceso</p>
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

<!-- ============ POR QUÉ NO INSTRUCCIÓN ============ -->
<section class="instruccion">
  <div class="wrap instr-grid">
    <div class="reveal">
      <p class="eyebrow">Una decisión de trabajo</p>
      <h2 class="h2">No acepto causas <em>en etapa de instrucción.</em></h2>
    </div>
    <div class="reveal">
      <p class="lead">La dedicación que requieren las situaciones cautelares y el trámite inicial del proceso es incompatible con el nivel de preparación que demanda el juicio.</p>
      <blockquote class="cita">La audiencia es la parte visible. El trabajo decisivo ocurre antes.</blockquote>
    </div>
  </div>
</section>
''' + cta(("Contame en qué instancia", "está la causa."), "Las consultas se evalúan según la instancia del caso y su complejidad; en función de eso defino la posibilidad de una entrevista.") + "\n</main>\n" + FOOTER
page("intervencion-en-juicio.html", interv)

# ================================================================== PREGUNTAS FRECUENTES
FAQ = [
 ("¿Estoy obligado a declarar en la indagatoria?", "No. El derecho a no declarar contra uno mismo está en el artículo 18 de la Constitución Nacional y en los tratados internacionales con jerarquía constitucional. La ley procesal agrega que el silencio no puede tomarse como presunción en contra."),
 ("Si no declaro, ¿el juez puede perjudicarme?", "Legalmente no: el silencio no puede usarse como prueba de culpabilidad ni fundar una condena. El riesgo real es el inverso. Una declaración improvisada, prestada sin conocer la prueba, puede condicionar la defensa en el juicio oral años después."),
 ("¿Se lee en el juicio oral lo que declaré en la investigación?", "Puede leerse, pero no sola. En el Código Procesal Penal de la Nación, el artículo 378 habilita esa lectura cuando el imputado se niega a declarar en el debate o cuando dice algo distinto de lo que había dicho antes. Como la mayoría de los imputados no declara al inicio del juicio, ese supuesto se da con mucha frecuencia. En los sistemas acusatorios el uso de las actas previas está más restringido, aunque no excluido."),
 ("¿Es un error admitir una parte de la imputación?", "Depende de la estrategia. Admitir presencia o discusión puede ser necesario, por ejemplo, en una legítima defensa. El problema aparece cuando esa admisión se hace sin una estrategia armada: ahí se consolidan gratuitamente los hechos que el fiscal todavía tenía que probar."),
 ("¿Cuándo es el momento correcto para declarar?", "Después de leer el expediente completo y de definir qué se va a sostener en el juicio. Declarar sin conocer la prueba de cargo ni el modo en que se va a desarrollar el debate rara vez es la mejor opción."),
 ("¿Vale lo mismo en CABA, en la Provincia de Buenos Aires y en el fuero federal?", "No. Las reglas sobre la incorporación por lectura de las declaraciones previas varían según el código procesal aplicable. Lo que se mantiene en todos los sistemas es el derecho a no declarar y el hecho de que lo dicho al inicio puede reaparecer en el debate."),
]
items = "\n".join(f'      <li><details><summary><span>{q}</span><i class="ti ti-plus" aria-hidden="true"></i></summary><div class="faq-a"><p>{a}</p></div></details></li>' for q, a in FAQ)
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
pf = head("Preguntas frecuentes | Declarar o no declarar · Leandro Sauchella",
  "¿Estoy obligado a declarar en la indagatoria? ¿Se lee en el juicio oral lo que declaré? Respuestas de un abogado penalista dedicado al juicio oral.", faq_ld
  ) + header("preguntas-frecuentes.html") + "\n<main>\n" + ph("palacio", "center 35%", "Preguntas frecuentes", ("Declarar", "o no declarar."),
  "Lo que se dice al inicio de una causa puede reaparecer años después en el juicio oral.") + f'''
<!-- ============ PREGUNTAS ============ -->
<section class="faq faq-page">
  <div class="wrap faq-page-in">
    <ul class="faq-list reveal">
{items}
    </ul>
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
