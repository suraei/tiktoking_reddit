# video_generator.py

import subprocess


def generar_video_con_audio(video_path: str, audio_path: str, output_path: str) -> None:
    """
    Combina un video con un audio externo usando ffmpeg.

    Args:
        video_path (str): Ruta del video base.
        audio_path (str): Ruta del audio generado.
        output_path (str): Ruta del archivo de salida.
    """
    try:
        print("🎞️ Generando video con audio...")

        command = [
            "ffmpeg",
            "-y",                        # sobrescribir sin preguntar
            "-i", video_path,
            "-i", audio_path,
            "-map", "0:v:0",             # usar solo video de input 0
            "-map", "1:a:0",             # usar solo audio de input 1
            "-c:v", "copy",
            "-c:a", "aac",
            "-shortest",
            output_path
        ]
        subprocess.run(command, check=True)
        print(f"✅ Video generado correctamente: {output_path}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"❌ Error al generar vídeo: {e}")


def agregar_subtitulos(video_path: str, srt_path: str, output_path: str) -> None:
    """
    Incrusta subtítulos visuales en un video con ffmpeg y libass.

    Args:
        video_path (str): Ruta del video fuente.
        srt_path (str): Ruta del archivo de subtítulos (.srt).
        output_path (str): Ruta del video con subtítulos embebidos.
    """
    try:
        print("💬 Agregando subtítulos...")

        command = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-vf", f"subtitles={srt_path}",
            "-c:a", "copy",
            output_path
        ]
        subprocess.run(command, check=True)
        print(f"✅ Subtítulos incrustados en el video: {output_path}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"❌ Error al agregar subtítulos: {e}")
