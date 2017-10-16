from skimage import *
def orderDither(img, dimension):
    img_out = img
    if dimension == 4:
        D = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
    if dimension == 2:
        D = [[0, 2], [3, 1]]
    wid = img.shape[0]
    hei = img.shape[1]
    for x in range(0, wid - 1):
        for y in range(0, hei - 1):
            i = x % dimension
            j = y % dimension
            print img[x, y]
            if img[x, y] * (dimension * dimension + 1) > D[j][i]:
                img_out[x, y] = 1
            else:
                img_out[x, y] = 0
    return img_out
