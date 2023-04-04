from PIL import Image

images = [f'{i}.jpg' for i in range(1, 6)]

for j in images:
    image = Image.open(j)
    watermark = Image.open("watermark.png")
    image.paste(watermark, (0, 0), watermark)
    image.save(f'watermarks/{j}')