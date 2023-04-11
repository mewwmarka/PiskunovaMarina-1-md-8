from PIL import Image
image = Image.open("otkritka.jpg")
image.crop((0, 0, 736, 240)).save("otkritka_crop.jpg")