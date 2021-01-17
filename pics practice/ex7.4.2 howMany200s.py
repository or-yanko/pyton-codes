from PIL import Image

img = Image.open("box.png")
img = img.resize((100, 100))
img3 = img.convert('L')

countColor = img.histogram()
print(countColor[199])