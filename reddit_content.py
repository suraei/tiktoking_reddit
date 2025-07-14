# reddit_content.py

import os
import requests
import argparse
from typing import List, Tuple


def get_top_post(subreddit: str, timeframe: str) -> Tuple[str, str]:
    """
    Obtiene el título y permalink del post más popular en un timeframe.

    Args:
        subreddit (str): Subreddit del cual extraer contenido.
        timeframe (str): 'day', 'week', 'month', 'year', 'all'.

    Returns:
        Tuple[str, str]: Título del post y permalink.
    """
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t={timeframe}&limit=1"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        post_data = response.json()["data"]["children"][0]["data"]
        return post_data["title"], post_data["permalink"]
    except Exception as e:
        raise RuntimeError(f"❌ Error al obtener el post: {e}")


def get_top_comments(permalink: str, limit: int) -> List[str]:
    """
    Dado un permalink, obtiene los comentarios más votados.

    Args:
        permalink (str): Enlace del post.
        limit (int): Cantidad de comentarios a devolver.

    Returns:
        List[str]: Comentarios.
    """
    url = f"https://www.reddit.com{permalink}.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        comments_data = response.json()[1]["data"]["children"]
        top_comments = [
            c["data"]["body"]
            for c in comments_data
            if "body" in c["data"]
        ][:limit]
        return top_comments
    except Exception as e:
        raise RuntimeError(f"❌ Error al obtener los comentarios: {e}")


def get_reddit_content(subreddit: str, timeframe: str, comment_limit: int) -> str:
    """
    Compone el texto final para TTS.

    Args:
        subreddit (str): Subreddit a usar.
        timeframe (str): Periodo de popularidad.
        comment_limit (int): Cantidad de respuestas a incluir.

    Returns:
        str: Texto completo.
    """
    title, permalink = get_top_post(subreddit, timeframe)
    comments = get_top_comments(permalink, comment_limit)

    full_script = f"Pregunta: {title}\n"
    for i, comment in enumerate(comments, start=1):
        full_script += f"Usuario de reddit {i} responde: {comment.strip()}\n"
    return full_script


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrae post y comentarios de Reddit para TTS")
    parser.add_argument("--subreddit", type=str, default="AskRedditespanol", help="Subreddit objetivo")
    parser.add_argument("--timeframe", type=str, default="day", choices=["hour", "day", "week", "month", "year", "all"], help="Periodo de tiempo")
    parser.add_argument("--limit", type=int, default=3, help="Cantidad de comentarios")

    args = parser.parse_args()

    print("🔎 Obteniendo contenido de Reddit...\n")
    try:
        script = get_reddit_content(args.subreddit, args.timeframe, args.limit)
        print(script)
    except Exception as error:
        print(error)
