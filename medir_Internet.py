import speedtest

def prueba_velocidad():
    print("Buscando el mejor servidor...\n")

    test = speedtest.Speedtest()

    test.get_best_server()

    # Descarga
    download = test.download() / 1_000_000

    # Subida
    upload = test.upload() / 1_000_000

    # Ping
    ping = test.results.ping

    print("=" * 40)
    print(f"Velocidad de descarga : {download:.2f} Mbps")
    print(f"Velocidad de subida   : {upload:.2f} Mbps")
    print(f"Ping                  : {ping:.2f} ms")
    print("=" * 40)

prueba_velocidad()