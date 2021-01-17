from PIL import Image

#func that gets create sqr image and draw a diagonal left up to right down
def ex1(n):
    imgNew = Image.new('L', (n, n), 255)#white new image
    mat = imgNew.load()
    for x in range(n):
        for y in range(n):
            if x % 10 == 0:
                mat[x, y] = 0

    return imgNew


def ex2(n):
    imgNew = Image.new('L', (n, n), 255)  # white new image
    mat = imgNew.load()
    for x in range(n):
        for y in range(n):
            if x % 20 == 0:
                mat[x, y] = 0

    return imgNew

#אחרי ייעול
def strips(n):
    imgNew = Image.new('L', (n, n), 255)  # white new image
    mat = imgNew.load()
    for x in range(0, n, 10):
        for y in range(n):
            mat[x, y] = 0

    return imgNew