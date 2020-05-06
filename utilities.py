import numpy as np

def calc_contrast_value(val, lo, hi):
    if val < lo:
        return 0
    if val > hi:
        return 1
    return (val - lo)/(hi - lo)


def contrast_image(img, low, high):
    res = [[calc_contrast_value(x, low, high) for x in y] for y in img]
    return np.array(res)


def change_resolution(img, factor):
    res = img[::factor, ::factor]
    return np.array(res)


def threshold(img, threshpoint):
    return np.array([[1 if x >= threshpoint else 0 for x in y] for y in img])