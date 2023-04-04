
from PIL import Image
image = Image.open("cat_meme.jpg")
image.show()
print(f'{image.size}\n{image.format}\n{image.mode}')


