from PIL import Image

img = Image.open("box.png")
#img.show() #show the pic
#print(img.size) #print the size of the pic
img2 = img.resize((100, 100))#change the size of image to 100,100
img3 = img.convert('L')#make black and white with 256 types of grey
mat3 = img3.load()#return the matrix that represent the image
mat3[100, 100] = 255#change the color of pixel
#if we enter number bigger than 256 it will change it to 256, and if under 0 it will be zero

#create new img
img4 = Image.new('L',(100,50),128)
img4.show();

