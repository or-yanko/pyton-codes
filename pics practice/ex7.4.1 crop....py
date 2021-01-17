from PIL import Image

img = Image.open("box.png")
img = img.resize((100, 100))
img3 = img.convert('L')
mat = img.load()

slice = img.crop((0, 0,50, 50))#crop the left up sqr
#slice.show()

imgRot = img.rotate(90)# rotate the img against the clock if num is positive, if negetive rotate with clock
#imgRot.show()

countColor = img.histogram()#how many from any color =histograma
print(countColor)
