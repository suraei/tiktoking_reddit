# 🎥 Reddia

Reddia es una herramienta que convierte publicaciones populares de Reddit en vídeos verticales, con narración por voz y subtítulos animados. Ideal para contenido corto en TikTok, Reels o Shorts. 🧠🗣️🎬

---

## ⚙️ ¿Qué hace?

✅ Extrae preguntas y respuestas populares de un subreddit  
✅ Genera audio con ElevenLabs (voz realista)  
✅ Añade subtítulos sincronizados  

---

## 📦 Requisitos

- Python 3.9 o superior 🐍  
- [FFmpeg](https://ffmpeg.org/) instalado en el sistema  
- Cuenta en [ElevenLabs](https://www.elevenlabs.io/) con clave API

---

## 🚀 Instalación

### 1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/reddia.git
cd reddia
```

### 2. Instala las dependencias

```bash pip install -r requirements.txt```

### 3. Crea un archivo api.json con tu clave de ElevenLabs:
```json
{
  "ELEVEN_API_KEY": "tu_clave_api_aquí"
}
```
### 4. Uso

Ejecuta el script principal con tus parámetros favoritos:

```bash
python main.py --subreddit AskRedditespanol --timeframe week --limit 3```

Opciones disponibles:
Argumento	Descripción	Valor por defecto
--subreddit	Subreddit del que se extraerá el contenido	AskRedditespanol
--timeframe	Periodo de popularidad: day, week, etc.	day
--limit	Número de respuestas a incluir en el vídeo	3
