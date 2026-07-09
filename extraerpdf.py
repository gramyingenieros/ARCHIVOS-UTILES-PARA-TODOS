from tkinter import Tk, filedialog
import pdfplumber
import os

# Oculta la ventana principal de tkinter
Tk().withdraw()

# Abre el explorador de Windows
archivo_pdf = filedialog.askopenfilename(
    title="Selecciona un archivo PDF",
    filetypes=[("Archivos PDF", "*.pdf")]
)

# Si el usuario cancela
if not archivo_pdf:
    print("No seleccionaste ningún archivo.")
    exit()

# Nombre del archivo TXT
archivo_txt = os.path.splitext(archivo_pdf)[0] + ".txt"

# Extrae el texto y lo guarda
with pdfplumber.open(archivo_pdf) as pdf, open(archivo_txt, "w", encoding="utf-8") as txt:

    for pagina in pdf.pages:
        texto = pagina.extract_text()

        if texto:
            txt.write(texto + "\n\n")

print("Extracción finalizada.")
print("Archivo guardado en:")
print(archivo_txt)