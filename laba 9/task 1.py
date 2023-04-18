from PIL import Image, ImageFilter
import os
if not os.path.exists("filters"):
    os.mkdir("filters")
for im in os.listdir('images'):
    image = Image.open(f'images/{im}')
    img_filter = image.filter(ImageFilter.SHARPEN)
    img_filter.save(f'filters/{im}')