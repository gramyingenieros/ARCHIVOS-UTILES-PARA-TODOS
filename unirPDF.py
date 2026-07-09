from tkinter import Tk, filedialog
from PyPDF2 import PdfMerger

# Ocultar ventana principal
root = Tk()
root.withdraw()

# Seleccionar varios PDF
archivos_pdf = filedialog.askopenfilenames(
    title="Selecciona los PDF que deseas unir",
    filetypes=[("Archivos PDF", "*.pdf")]
)

if archivos_pdf:
    merger = PdfMerger()

    for pdf in archivos_pdf:
        merger.append(pdf)

    # Elegir dónde guardar el PDF final
    salida = filedialog.asksaveasfilename(
        title="Guardar PDF unido como",
        defaultextension=".pdf",
        filetypes=[("Archivo PDF", "*.pdf")]
    )

    if salida:
        merger.write(salida)
        merger.close()
        print("PDF unido correctamente.")
    else:
        print("No seleccionaste dónde guardar el archivo.")
else:
    print("No seleccionaste ningún PDF.")