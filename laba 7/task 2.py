from PIL import Image
image = Image.open("cat_meme.jpg")
resize_image = image.reduce(3)
resize_image.save("cat_meme_resize.jpg")
transposed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
transposed_image.save("cat_meme_transposed.jpg")
transposed2_image = image.transpose(Image.FLIP_TOP_BOTTOM)
transposed2_image.save("cat_meme_transposed2.jpg")