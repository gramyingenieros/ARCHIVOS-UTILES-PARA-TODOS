import pandas as pd
from tkinter import Tk, filedialog


def seleccionar_archivos():
    Tk().withdraw()  # Oculta la ventana principal

    archivos = filedialog.askopenfilenames(
        title="Selecciona los archivos Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )

    return list(archivos)


def unir_excel():
    archivos = seleccionar_archivos()

    if not archivos:
        print("No seleccionaste ningún archivo.")
        return

    dataframes = []

    for archivo in archivos:
        try:
            df = pd.read_excel(archivo)
            dataframes.append(df)
            print(f"✔ Archivo cargado: {archivo}")
        except Exception as e:
            print(f"✘ Error al leer {archivo}")
            print(e)

    if not dataframes:
        print("No se pudo leer ningún archivo.")
        return

    df_final = pd.concat(dataframes, ignore_index=True)

    salida = filedialog.asksaveasfilename(
        title="Guardar archivo combinado",
        defaultextension=".xlsx",
        filetypes=[("Excel", "*.xlsx")],
        initialfile="Archivo_Combinado.xlsx"
    )

    if salida:
        df_final.to_excel(salida, index=False)
        print("\n======================================")
        print("✅ Archivos unidos correctamente.")
        print(f"📄 Total de archivos: {len(archivos)}")
        print(f"📊 Total de filas: {len(df_final)}")
        print(f"💾 Guardado en: {salida}")
        print("======================================")
    else:
        print("Operación cancelada.")


if __name__ == "__main__":
    unir_excel()