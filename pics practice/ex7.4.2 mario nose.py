from PIL import Image

img = Image.open("box.png")
img3 = img.convert('L')

cropedImg = img.crop((95, 88,150, 132))#crop

cropedImg.show()