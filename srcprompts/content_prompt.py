BLOG_TEMPLATE = """
Eres un escritor experto en blogs con amplia experiencia en SEO y storytelling.

Tema del blog: {topic}
Tono: {tone}
Longitud: {length}

Escribe un artículo de blog completo con la siguiente estructura:
- Título atractivo con gancho
- Introducción que enganche al lector en las primeras líneas
- Desarrollo con subtítulos (H2/H3) bien organizados
- Ejemplos o datos concretos cuando sea relevante
- Conclusión con llamada a la acción

El artículo debe estar optimizado para lectura web (párrafos cortos, subtítulos claros).

Artículo:
"""

X_TEMPLATE = """
Eres un experto en Twitter/X con dominio del formato viral y engagement.

Tema: {topic}
Tono: {tone}
Formato: {length}

Crea el contenido para X (Twitter) siguiendo estas reglas:
- Si es un tweet único: máximo 280 caracteres, directo e impactante
- Si es un hilo: entre 5 y 10 tweets numerados (1/, 2/, 3/...), cada uno con gancho
- Usa emojis estratégicamente sin exagerar
- El primer tweet debe ser el más impactante para generar clicks
- Incluye hashtags relevantes al final (máximo 3)

Contenido para X:
"""

LINKEDIN_TEMPLATE = """
Eres un experto en personal branding y contenido profesional para LinkedIn.

Tema: {topic}
Tono: {tone}
Longitud: {length}

Escribe un post de LinkedIn con esta estructura:
- Primera línea gancho (máximo 2 líneas, debe generar el "ver más")
- Historia o contexto personal/profesional relacionado al tema
- Insight o aprendizaje clave
- Puntos de valor en formato lista (usa emojis como bullets)
- Cierre con pregunta para generar comentarios o llamada a la acción
- Entre 3 y 5 hashtags profesionales al final

El tono debe ser profesional pero humano, evita el lenguaje corporativo frío.

Post de LinkedIn:
"""

EMAIL_TEMPLATE = """
Eres un experto en email marketing y comunicación corporativa efectiva.

Tema del correo: {topic}
Tono: {tone}
Longitud: {length}

Redacta un correo electrónico completo con:
- Asunto: atractivo y claro (máximo 60 caracteres)
- Saludo apropiado
- Cuerpo del mensaje bien estructurado con párrafos cortos
- Llamada a la acción clara y específica
- Cierre profesional con firma placeholder

El correo debe ser directo, respetar el tiempo del lector y tener un único objetivo claro.

Correo:
"""

VIDEO_TEMPLATE = """
Eres un guionista experto en contenido para YouTube, TikTok y Reels.

Tema del video: {topic}
Tono: {tone}
Duración aproximada: {length}

Escribe un guión de video con este formato:
- [GANCHO] (primeros 3-5 segundos): frase o pregunta que detenga el scroll
- [INTRODUCCIÓN] (10-15 segundos): presenta el tema y qué va a aprender el espectador
- [DESARROLLO]: puntos principales con indicaciones de escena o transición entre corchetes
- [CIERRE]: resumen del valor entregado
- [CTA]: llamada a la acción final (suscribirse, comentar, seguir, etc.)

Incluye indicaciones de ritmo, pausas o énfasis donde sea necesario.

Guión:
"""

PROMPTS = {
    "Blog": (BLOG_TEMPLATE, ["topic", "tone", "length"]),
    "X (Twitter)": (X_TEMPLATE, ["topic", "tone", "length"]),
    "LinkedIn": (LINKEDIN_TEMPLATE, ["topic", "tone", "length"]),
    "Correo electrónico": (EMAIL_TEMPLATE, ["topic", "tone", "length"]),
    "Guión de video": (VIDEO_TEMPLATE, ["topic", "tone", "length"]),
}
