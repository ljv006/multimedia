#coding=utf-8

def colorDither(img, look_up_table):
    wid = img.shape[0]
    hei = img.shape[1]
    for x in range(0, wid - 1):
        for y in range(0, hei - 1):
            color_list = img[x, y]
            R = color_list[0]
            G = color_list[1]
            B = color_list[2]
            for color_R in look_up_table[0]:
                if abs(R - color_R) < 16:
                    img[x,y][0] = color_R
                    break
            for color_G in look_up_table[1]:
                if abs(G - color_G) < 16:
                    img[x,y][1] = color_G
                    break
            for color_B in look_up_table[2]:
                if abs(B - color_B) < 16:
                    img[x,y][2] = color_B
                    break
    return img

def colorDitherWithoutLUT(img):
    wid = img.shape[0]
    hei = img.shape[1]
    R_channel = img[:, :, 0]
    G_channel = img[:, :, 1]
    B_channel = img[:, :, 2]

    return img