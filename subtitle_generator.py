# subtitle_generator.py

import os
import subprocess


def generar_subtitulos(audio_path: str, srt_output_path: str) -> None:
    """
    Genera un archivo .srt con subtítulos sincronizados usando Whisper (CLI).

    Args:
        audio_path (str): Ruta del archivo de audio de entrada.
        srt_output_path (str): Ruta donde guardar el archivo de subtítulos .srt.
    """
    print("🧠 Transcribiendo audio con Whisper...")

    try:
        # Whisper CLI genera los subtítulos en el mismo directorio del audio
        command = [
            "whisper",
            audio_path,
            "--model", "base",               # Puedes cambiar a 'medium' o 'large' si necesitas más calidad
            "--language", "es",
            "--task", "transcribe",
            "--output_format", "srt"
        ]

        subprocess.run(command, check=True)

        # Whisper crea el archivo con el mismo nombre base que el audio
        nombre_base = os.path.splitext(audio_path)[0]
        generado = f"{nombre_base}.srt"

        if not os.path.exists(generado):
            raise FileNotFoundError(f"No se encontró el archivo generado: {generado}")

        os.rename(generado, srt_output_path)
        print(f"✅ Subtítulos generados: {srt_output_path}")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"❌ Error en whisper: {e}")
    except Exception as e:
        raise RuntimeError(f"❌ Error al generar subtítulos: {e}")
