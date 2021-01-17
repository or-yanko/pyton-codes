from PIL import Image

#q7
def chess(n):
    img = Image.new('L',(n,n), 255)
    mat = img.load()
    for x in range(n):
        for y in range(n):
            if (x + y) % 2 == 0:
                mat[x,y]=0
    img.show()
    return img

#q8
def border(n):
    mat = img.load()
    for x in range(n):
        for y in range(n):
            if x == 0 or y == 0 or x == n-1 or y == n-1:
                mat[x, y] = 0
    img.show()
    return img

#q9
def square1(img):
    img2 = img.copy()

    w1, h1 = img2.size

    mat = img2.load()
    for x in range(20):
        for y in range(20):
            mat[x, h1 - 1 - y] = 255
    img2.show()
    return img2

#q10
def black_white(img):
    img2 = img.copy()
    img2 = img2.convert('L')
    w, h = img2.size
    mat = img2.load()
    sum = 0
    for x in range(w):
        for y in range(h):
            sum += mat[x, y]
    avg = sum / (w * h)

    for x in range(w):
        for y in range(h):
            if mat[x, y] < avg:
                mat[x, y] = 0
            else:
                mat[x, y] = 255
    img2.show()
    return img2



img = Image.open("box.png")
black_white(img)