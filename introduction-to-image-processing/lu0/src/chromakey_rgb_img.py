import numpy as np
from skimage.color import rgb2hsv, hsv2rgb
from skimage.transform import resize

def chromakey_filter_rgb_img(original_img, replacement_img, hue_range):
    """
    replaces every pixel of the image matched by the hue range by the 
    corresponding pixel in the other image, resizing the replacement image if necessary

    args:
        original_img (numpy.array rgb image): the image which will have pixels keyed out
        replacement_img (numpy.array rgb image): the image which will have pixels keyed in
        hue_range (tuple[(0-360), (0-360)]): the range within which pixels will be keyed out

    returns:
        (numpy.array rgb image): the modified image
    """
    hsv_img = rgb2hsv(original_img)

    replacement_img = resize(rgb2hsv(replacement_img), (hsv_img.shape[0], hsv_img.shape[1]))

    for x, row in enumerate(hsv_img):

        for y, pixel in enumerate(row):

            hue, saturation, lightness = pixel

            is_in_hue_range = hue > hue_range[0] and hue < hue_range[1]

            if is_in_hue_range:
 
                hsv_img[x, y] = replacement_img[x, y]

    return (hsv2rgb(hsv_img) * 255).astype(np.uint8)