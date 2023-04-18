from PIL import Image, ImageFilter
import os
if not os.path.exists("filters"):
    os.mkdir("filters")
im_list = [im for im in os.listdir('images') if im.endswith('.jpg')]
for im in im_list:
    image = Image.open(f'images/{im}')
    img_filter = image.filter(ImageFilter.SHARPEN)
    img_filter.save(f'filters/{im}')