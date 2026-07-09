import subprocess


def obtener_redes_wifi():
    try:
        resultado = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            encoding="utf-8",
            errors="ignore"
        )

        redes = [
            linea.split(":")[1].strip()
            for linea in resultado.splitlines()
            if "All User Profile" in linea
        ]

        return redes

    except Exception as e:
        print("Error al obtener las redes WiFi.")
        print(e)
        return []


def mostrar_contrasena(nombre_wifi):
    try:
        resultado = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", nombre_wifi, "key=clear"],
            encoding="utf-8",
            errors="ignore"
        )

        print("\n" + "=" * 60)
        print(f"Información de la red: {nombre_wifi}")
        print("=" * 60)
        print(resultado)

    except Exception as e:
        print("No fue posible obtener la información.")
        print(e)


def main():

    redes = obtener_redes_wifi()

    if not redes:
        print("No se encontraron redes WiFi guardadas.")
        return

    print("\nRedes WiFi almacenadas:\n")

    for i, red in enumerate(redes, start=1):
        print(f"{i}. {red}")

    while True:
        try:
            opcion = int(input("\nSelecciona una red: "))

            if 1 <= opcion <= len(redes):
                break

            print("Número fuera de rango.")

        except ValueError:
            print("Ingresa únicamente números.")

    mostrar_contrasena(redes[opcion - 1])


if __name__ == "__main__":
    main()