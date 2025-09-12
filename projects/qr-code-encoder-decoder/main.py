import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def qr_encoder():

    data = "https://mabbas.vercel.app/"

    img = qrcode.make(data)

    img.save("qrcode.png")

qr_encoder()


def qr_decoder():
    
    img = Image.open("C:/Users/Lenovo/Desktop/Python/assignments/qr-code-encoder-decoder/qrcode.png")
    # img = Image.open("qrcode.png")

    result = decode(img)

    print(result)

# qr_decoder()  # uncomment and run this if you have already executed first