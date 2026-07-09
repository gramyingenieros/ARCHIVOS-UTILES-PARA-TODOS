import qrcode

texto = input("Ingrese el texto o enlace: ")

qr = qrcode.make(texto)

qr.save(".png")

qr.show()

print("✅ Código QR generado correctamente.")