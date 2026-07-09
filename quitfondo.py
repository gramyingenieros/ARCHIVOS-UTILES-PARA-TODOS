from rembg import remove
from PIL import Image
from tkinter import Tk, filedialog
import os

# Ocultar la ventana principal de Tkinter
Tk().withdraw()

# Seleccionar la imagen

input_path = filedialog.askopenfilename(
    title="Selecciona una imagen",
    filetypes=[
        ("Imágenes", "*.png *.jpg *.jpeg *.bmp *.webp")
    ]
)

if input_path:
    # Crear nombre del archivo de salida

    carpeta = os.path.dirname(input_path)
    nombre = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(carpeta, f"{nombre}_sin_fondo.png")

    # Procesar imagen

    imagen = Image.open(input_path)
    salida = remove(imagen)
    salida.save(output_path)

    print("Imagen guardada en:")
    print(output_path)

    # Abrir resultado

    Image.open(output_path).show()
else:
    print("No seleccionaste ninguna imagen.")