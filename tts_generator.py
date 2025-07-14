"""
tts_generator.py

Módulo para convertir texto a audio usando ElevenLabs.
Diseñado para ser fácilmente extensible a otros motores TTS en el futuro.
"""

import json
import os
import requests


def _cargar_api_key(archivo: str = "api.json") -> str:
    """
    Carga la clave API de un archivo JSON.

    Args:
        archivo (str): Ruta del archivo JSON que contiene la API key.

    Returns:
        str: Clave API.
    """
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
            return datos.get("ELEVEN_API_KEY", "")
    except Exception as e:
        raise RuntimeError(f"❌ No se pudo cargar la clave API desde '{archivo}': {e}")


def generar_audio(
    texto: str,
    output_path: str = "output.mp3",
    engine: str = "elevenlabs",
    voice_id: str = "TxGEqnHWrfWFTfGW9XjX"
) -> None:
    """
    Convierte texto a audio usando el motor especificado.

    Args:
        texto (str): Texto a sintetizar.
        output_path (str): Ruta donde guardar el archivo de audio.
        engine (str): Motor de TTS a usar (por ahora solo 'elevenlabs').
        voice_id (str): ID de la voz a usar en ElevenLabs.
    """
    if engine == "elevenlabs":
        _tts_elevenlabs(texto, output_path, voice_id)
    else:
        raise ValueError(f"⚠️ Motor TTS no soportado: '{engine}'")


def _tts_elevenlabs(texto: str, output_path: str, voice_id: str) -> None:
    """
    Función interna para generar audio usando ElevenLabs API.

    Args:
        texto (str): Texto a convertir.
        output_path (str): Ruta donde guardar el archivo mp3.
        voice_id (str): ID de la voz a usar.
    """
    api_key = _cargar_api_key()
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.8
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Audio guardado en '{output_path}' usando ElevenLabs.")
    except Exception as e:
        raise RuntimeError(f"❌ Error al generar audio con ElevenLabs: {e}")


# Test individual del módulo
if __name__ == "__main__":
    texto_prueba = (
        "Pregunta: ¿Qué harías si volvieras a tener 10 años?\n"
        "Respuesta 1: Me enfocaría en aprender lo que realmente importa.\n"
        "Respuesta 2: Pasaría más tiempo con mi familia."
    )

    try:
        print("🔊 Generando audio de prueba...")
        generar_audio(texto_prueba, "audio_prueba.mp3")
    except Exception as error:
        print(error)
