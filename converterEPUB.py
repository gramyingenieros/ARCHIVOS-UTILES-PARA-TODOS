from tkinter import Tk, filedialog
from pypdf import PdfReader
from ebooklib import epub

# Ocultar la ventana principal de Tkinter
Tk().withdraw()

# Seleccionar el PDF
ruta_pdf = filedialog.askopenfilename(
    title="Seleccionar archivo PDF",
    filetypes=[("Archivos PDF", "*.pdf")]
)

# Verificar si el usuario seleccionó un archivo
if not ruta_pdf:
    print("No se seleccionó ningún archivo.")
    exit()

# Leer el PDF
reader = PdfReader(ruta_pdf)

texto = ""

for page in reader.pages:
    contenido = page.extract_text()
    if contenido:
        texto += contenido + "\n\n"

# Crear el EPUB
book = epub.EpubBook()
book.set_identifier("001")
book.set_title("Libro Convertido")
book.set_language("es")
book.add_author("Conversión Automática")

chapter = epub.EpubHtml(
    title="Contenido",
    file_name="contenido.xhtml",
    lang="es"
)

chapter.content = f"<h1>Contenido</h1><p>{texto.replace('\n', '<br>')}</p>"

book.add_item(chapter)

book.toc = (epub.Link("contenido.xhtml", "Contenido", "contenido"),)
book.spine = ["nav", chapter]

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Elegir dónde guardar el EPUB
ruta_guardado = filedialog.asksaveasfilename(
    title="Guardar EPUB",
    defaultextension=".epub",
    filetypes=[("Archivo EPUB", "*.epub")]
)

if ruta_guardado:
    epub.write_epub(ruta_guardado, book)
    print("✅ EPUB creado correctamente.")
else:
    print("Conversión cancelada.")