from PIL import Image

img = Image.open("box.png")
img = img.resize((100, 100))#change the size of image to 100,100
img3 = img.convert('L')#make black and white with 256 types of grey
mat = img.load()#return the matrix that represent the image

for x in range(40):
    for y in range(40):
        mat[99-x, 99-y] = 128
img.show()



