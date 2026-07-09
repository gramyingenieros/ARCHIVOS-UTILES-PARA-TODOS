import yt_dlp

def download_yt_video(url):
    opciones = {
        "format": "best[ext=mp4]/best",
        "outtmpl": "%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": False
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("Ingrese la URL del video: ")
    download_yt_video(video_url)