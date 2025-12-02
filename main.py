import qrcode

url = "https://github.com/Klaxigon/1-Year-with-my-Girlfriend/blob/main/loveletter.txt"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("loveletter_qr.png")

print("QR-Code für die Webseite erstellt!")