#! /usr/bin/python3

"""introduction to image processing - ulrich von zadow - 0 - 15.09.2022"""

from os.path import abspath, join

from skimage.io import imread, imsave
from skvideo.io import vwrite

from apply_gamma_filter import apply_gamma_filter
from chromakey_rgb_img import chromakey_filter_rgb_img
from shift_hue import shift_hue



# scikit's default pixel format is yuvj444p, this is not playable by most video players
VIDEO_OPTIONS = {
    "-pix_fmt": "yuvj420p"
}
DIR = abspath(join(__file__, "../.."))

def main():
    soeder_img = imread(f"{DIR}/in/linus-bolls-cv.jpg")
    amp_img = imread(f"{DIR}/in/amp-backside.jpg")

    # crispify maggus his likeness
    filtered_img = apply_gamma_filter(soeder_img, 6)
    imsave(f"{DIR}/out/gamma-shifted-soeder.jpg", filtered_img)

    # replace maggus his face with my guitar amplifier
    keyed_img = chromakey_filter_rgb_img(soeder_img, amp_img, (0, 0.5))
    imsave(f"{DIR}/out/keyed-soeder.jpg", keyed_img)

    # create 50 frames of pure soeder goodness
    disco_frames = [shift_hue(soeder_img, i / 3) for i in range(50)]
    vwrite(f"{DIR}/out/disco-soeder.mp4", disco_frames, outputdict=VIDEO_OPTIONS)

if __name__ == "__main__":
    main()