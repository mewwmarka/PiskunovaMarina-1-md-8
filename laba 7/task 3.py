from PIL import Image, ImageFilter

images = [f'{i}.jpg' for i in range(1, 6)]

for j in images:
    image = Image.open(j)
    img_filter = image.filter(ImageFilter.SHARPEN)
    img_filter.save(f'filters/{j}')
