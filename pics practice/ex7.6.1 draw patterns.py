from PIL import Image
import  random

#func that gets create sqr image and draw a diagonal left up to right down
def digonal(n):
    imgNew = Image.new('L', (n, n), 255) #white new image
    mat = imgNew.load()
    for i in range(n):
        mat[n, n] = 0
    return imgNew

#make salt and peper noises
def add_sp(img, p):
    w, h = img.size
    mat = img.load()
    noisy_img = img.copy()
    noisy_mat = noisy_img.load()
    for x in range(w):
        for y in range(h):
            r = random.random()
            if r < p:
                if r < p / 2:
                    noisy_mat[x, y] = 0
                else:
                    noisy_mat[x, y] = 255

    return noisy_img

#clean salt and peper noises
def items(mat, x, y):
    # flatten 3-by-3 square elements around mat[x,y] into a list
    lst = []
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            lst.append(mat[a, b])
    return lst
def median(lst):
    sort_lst = sorted(lst)
    n = len(sort_lst)
    return sort_lst[n // 2]

def clean_sp(img):
    # cleans salt and pepper noise from mat
    w, h = img.size
    mat = img.load()
    clean_img = img.copy()
    clean_mat = clean_img.load()
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if (mat[x, y] == 0) or (mat[x, y] == 255):  # needs cleaning
                clean_mat[x, y] = median(items(mat, x, y))

    return clean_img


print(1000//3)