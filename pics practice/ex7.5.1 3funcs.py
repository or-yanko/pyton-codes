from PIL import Image

img = Image.open("box.png")
img = img.resize((100, 100))#change the size of image to 100,100
img3 = img.convert('L')#make black and white with 256 types of grey

#get image and integer k, make the image brighter k times
def brighter(image, k):
    w, h = image.size
    imgNew = image.copy()
    mat = imgNew.load()
    for x in range(h):
        for y in range(h):
            mat[x, y] = int(mat[x, y]) + int(k)
    return imgNew

#get image and return its negative
def nerative(image):
    w, h = image.size
    imgNew = image.copy()
    mat = imgNew.load()
    for x in range(h):
        for y in range(h):
            mat[x, y] = 255 - mat[x, y]
    return imgNew

#hipuch of image up down
def hipuchud(image):
    w, h = image.size
    imgNew = Image.new('L', (w, h), 255)

    mat = image.load()
    matNew = imgNew.load()

    for x in range(w):
        for y in range(h):
            matNew[x, y] = mat[x, (h - 1 - y)]
    return imgNew

#hipuch of image left right
def hipuchlr(image):
    imgNew = image.copy()
    w, h = imgNew.size

    mat = image.load()
    matNew = imgNew.load()

    for x in range(w):
        for y in range(h):
            matNew[x, y] = mat[w - 1 - x, y]
    return imgNew
q = Image.open("box.png")

c = brighter(q,int(50))
d = nerative(q)