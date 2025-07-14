# main.py

import argparse
from reddit_content import get_reddit_content
from tts_generator import generar_audio
from subtitle_generator import generar_subtitulos
from video_generator import generar_video_con_audio, agregar_subtitulos

BACKGROUND_VIDEO = "background.mp4"
AUDIO_FILE = "reddit_audio.mp3"
SRT_FILE = "subtitulos.srt"
VIDEO_FINAL = "output_final.mp4"
VIDEO_SUBTITULADO = "output_con_subtitulos.mp4"


def main():
    parser = argparse.ArgumentParser(description="Genera video narrado con subtítulos a partir de Reddit.")
    parser.add_argument("--subreddit", type=str, default="AskRedditespanol", help="Subreddit a usar")
    parser.add_argument("--timeframe", type=str, default="day", choices=["hour", "day", "week", "month", "year", "all"], help="Periodo de popularidad")
    parser.add_argument("--limit", type=int, default=3, help="Cantidad de respuestas a incluir")

    args = parser.parse_args()

    try:
        print("🧠 Obteniendo contenido de Reddit...")
        texto = get_reddit_content(args.subreddit, args.timeframe, args.limit)

        print("🗣️ Generando audio...")
        generar_audio(texto, AUDIO_FILE)

        print("💬 Generando subtítulos...")
        generar_subtitulos(AUDIO_FILE, SRT_FILE)

        print("🎞️ Generando vídeo final...")
        generar_video_con_audio(BACKGROUND_VIDEO, AUDIO_FILE, VIDEO_FINAL)

        print("📺 Incrustando subtítulos...")
        agregar_subtitulos(VIDEO_FINAL, SRT_FILE, VIDEO_SUBTITULADO)

        print(f"✅ Vídeo final listo: {VIDEO_SUBTITULADO}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
