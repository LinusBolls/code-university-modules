import numpy as np
from skimage.color import rgb2lab, lab2lch, lab2rgb, lch2lab

def shift_hue(rgb_img, rotation):
    """
    shifts the hue of the image by the rotation value, maintaining the 
    perceived lightness by intermediate conversion to the 
    lch color format (see: https://en.wikipedia.org/wiki/hcl_color_space)

    args:
            rgb_img (numpy.array rgb image): the input image
            rotation (0-360): the amount by which to shift the hue

    returns:
            (numpy.array rgb image): the modified image
    """
    lch_img = lab2lch(rgb2lab(rgb_img))

    for x, row in enumerate(lch_img):

        for y, pixel in enumerate(row):

            lightness, chroma, hue = pixel

            new_hue = hue + rotation

            new_pixel = lightness, chroma, new_hue

            lch_img[x, y] = new_pixel

    return (lab2rgb(lch2lab(lch_img)) * 255).astype(np.uint8)