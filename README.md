# ✍️ Generador de Contenido con IA

Aplicación web que genera contenido textual personalizado usando modelos de lenguaje. Soporta ejecución **local con Ollama** o en la **nube con Groq**, con prompts especializados para cada tipo de contenido.

---

## 🚀 Demo

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)

---

## ✨ Funcionalidades

- 🎯 **5 tipos de contenido** con prompts especializados: Blog, X (Twitter), LinkedIn, Correo electrónico y Guión de video
- ⚡ **Streaming en tiempo real** — el texto aparece token a token mientras se genera
- 🔀 **Doble proveedor** — elige entre Ollama (local) o Groq (nube) desde la interfaz
- 🎨 **Personalización** — selecciona tono, longitud y modelo desde la UI
- 💾 **Descarga directa** del contenido generado en `.txt`

---

## 🗂️ Estructura del Proyecto

```
mod3-project3-Karina/
├── app.py                        # Interfaz principal con Streamlit
├── .env                          # Variables de entorno (no incluido en git)
├── .gitignore
├── requirements.txt
├── src/
│   ├── llm.py                    # Configuración de Ollama y Groq
│   ├── chains.py                 # Construcción de cadenas LangChain
│   └── utils.py                  # Funciones auxiliares
└── srcprompts/
    └── content_prompt.py         # Prompts especializados por categoría
```

---

## 🧠 Prompts Especializados

Cada tipo de contenido tiene su propio prompt con instrucciones específicas de formato y estructura:

| Tipo | Descripción |
|------|-------------|
| 📝 **Blog** | Artículo completo con estructura SEO, subtítulos H2/H3 y CTA |
| 🐦 **X (Twitter)** | Tweet único (280 chars) o hilo numerado con hashtags |
| 💼 **LinkedIn** | Post profesional con gancho, historia, insights y hashtags |
| 📧 **Correo electrónico** | Email completo con asunto optimizado, cuerpo y CTA |
| 🎬 **Guión de video** | Guión con secciones [GANCHO], [INTRO], [DESARROLLO], [CTA] |

---

## ⚙️ Proveedores de LLM

### 🖥️ Ollama (Local)
Ejecuta el modelo directamente en tu máquina. Sin costos, sin límites, sin internet.

| Modelo | RAM recomendada |
|--------|----------------|
| `llama3` | 8 GB |
| `mistral` | 8 GB |
| `gemma` | 6 GB |
| `phi3` | 4 GB |

### ☁️ Groq (Nube)
API gratuita con hardware especializado (LPU). Mucho más rápido que ejecución local.

| Modelo | Descripción |
|--------|-------------|
| `openai/gpt-oss-20b` | 20B parámetros, rápido |
| `openai/gpt-oss-120b` | 120B parámetros, mayor calidad |
| `qwen/qwen3.8-27b` | Modelo Qwen 27B |
| `allam-2-7b` | Modelo ligero 7B |

---

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Bootcamp-IA-MAD-P7/mod3-project3-Karina.git
cd mod3-project3-Karina
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
OLLAMA_MODEL=llama3
GROQ_API_KEY=tu_api_key_aqui
GROQ_MODEL=openai/gpt-oss-20b
```

> Obtén tu API Key gratuita en [console.groq.com](https://console.groq.com)

### 4. (Solo Ollama) Instalar y descargar el modelo

Descarga Ollama desde [ollama.com](https://ollama.com) y luego:

```bash
ollama pull llama3
```

### 5. Ejecutar la aplicación

```bash
python -m streamlit run app.py
```

Abre tu navegador en `http://localhost:8501`

---

## 🔧 Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Interfaz | Streamlit |
| Orquestación LLM | LangChain |
| LLM Local | Ollama |
| LLM Nube | Groq |
| Variables de entorno | python-dotenv |
| Lenguaje | Python 3.10+ |

---

## 📋 Requisitos

```
langchain
langchain-community
langchain-ollama
langchain-groq
streamlit==1.41.1
starlette==0.41.3
python-dotenv
```

---

## 🤝 Contribuciones

¿Quieres añadir un nuevo tipo de contenido? Solo necesitas agregar un nuevo template en `srcprompts/content_prompt.py` y añadirlo al diccionario `PROMPTS`. Aparecerá automáticamente en la UI sin tocar `app.py`.

```python
MI_TEMPLATE = """
Eres experto en...
Tema: {topic}
Tono: {tone}
Longitud: {length}
...
"""

PROMPTS["Mi categoría"] = (MI_TEMPLATE, ["topic", "tone", "length"])
```
