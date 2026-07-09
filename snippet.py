from tkinter import Tk, filedialog
from pdf2docx import Converter
import os

# Oculta la ventana principal de tkinter

Tk().withdraw()

# Seleccionar el PDF

archivo_pdf = filedialog.askopenfilename(
    title="Selecciona un archivo PDF",
    filetypes=[("Archivos PDF", "*.pdf")]
)

# Si el usuario cancela

if not archivo_pdf:
    print("No se seleccionó ningún archivo.")
    exit()

# Crear el nombre del Word automáticamente

archivo_docx = os.path.splitext(archivo_pdf)[0] + ".docx"

# Convertir
cv = Converter(archivo_pdf)
cv.convert(archivo_docx)
cv.close()

print("Conversión finalizada.")
print("Archivo guardado en:")
print(archivo_docx)