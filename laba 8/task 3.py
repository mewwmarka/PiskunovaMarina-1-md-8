from PIL import Image, ImageDraw, ImageFont
image = Image.open("otkritka.jpg")
name = input("Кого вы хотите поздравить? ").capitalize()
text = ImageDraw.Draw(image)
font = ImageFont.truetype("font.otf", size=24)
text.text(
    xy=(250, 700),
    text=f'{name} поздравляю!',
    fill="#FAACAC",
    font=font
)
text.text(
    xy=(251, 701),
    text=f'{name} поздравляю!',
    fill="#FAACAC",
    font=font
)
text.text(
    xy=(249, 699),
    text=f'{name} поздравляю!',
    fill="#FAACAC",
    font=font
)
image.show()
image.save("otkritka_text.png")

