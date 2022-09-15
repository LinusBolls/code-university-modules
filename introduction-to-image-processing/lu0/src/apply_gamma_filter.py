import numpy as np
from skimage.color import rgb2hsv, hsv2rgb

def apply_gamma_filter(rgb_img, factor):
    """
    factorizes the brightness of each pixel by the factor,
    darkening the dark parts and lightening the light parts of the image
    (see: https://en.wikipedia.org/wiki/Gamma_correction)

    args:
            rgb_img (numpy.array rgb image): the input image
            factor (int): the amount by which to modify the lightness

    returns:
            (numpy.array rgb image): the modified image
    """
    hsv_img = rgb2hsv(rgb_img)

    for x, row in enumerate(hsv_img):

        for y, pixel in enumerate(row):

            hue, saturation, lightness = pixel

            new_lightness = lightness ** factor

            new_pixel = hue, saturation, new_lightness

            hsv_img[x, y] = new_pixel

    return (hsv2rgb(hsv_img) * 255).astype(np.uint8)