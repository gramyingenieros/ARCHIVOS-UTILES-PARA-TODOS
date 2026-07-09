#SIRVE PARA CONVERTIR ARCHIVOS Y/O VIDEOS (MP4 a MP3)

from tkinter import Tk, filedialog
from moviepy import VideoFileClip
import os

# Oculta la ventana principal de tkinter

Tk().withdraw()

# Abre el explorador de Windows

archivo_video = filedialog.askopenfilename(
    title="Selecciona un video",
    filetypes=[("Videos", "*.mp4 *.avi *.mov *.mkv")]
)

# Si el usuario cancela
if not archivo_video:
    print("No seleccionaste ningún video.")
    exit()

# Nombre del MP3

archivo_mp3 = os.path.splitext(archivo_video)[0] + ".mp3"

# Conversión

clip = VideoFileClip(archivo_video)
clip.audio.write_audiofile(archivo_mp3)
clip.close()

print("Conversión finalizada.")
print("Archivo guardado en:")
print(archivo_mp3)