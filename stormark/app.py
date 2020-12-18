"""
StorMark application.

A tool for generating perceptual attacks to images and, possibly, video.
"""
import glob
import os

import numpy as np

from argparse import ArgumentParser

from PIL import Image

from stormark.attacks.correction import BrightnessCorrection, ContrastCorrection, GammaCorrection
from stormark.attacks.additive_noise import GaussianNoise

def main():
    parser = ArgumentParser(description="Image attack")
    parser.add_argument("input", help="path to the folder to be manipulated")
    parser.add_argument("output", help="path to the folder to store the manipulated images")

    brightness_intensities = [0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.2, 1.3, 1.4, 1.5]
    contrast_intensities = [0.5, 0.6, 0.7, 0.8, 0.9]
    gaussian_intensities = np.arange(0, 0.5001, 0.05)
    gamma_intensities = [1.18]
    brightness = BrightnessCorrection()
    contrast = ContrastCorrection()
    gamma = GammaCorrection()
    gaussian_noise = GaussianNoise()

    args = parser.parse_args()

    for imgpath in glob.glob(os.path.join(args.input, "*")):
        basename = os.path.basename(imgpath)
        basename = ".".join(basename.split(".")[:-1])

        img = Image.open(imgpath)

        folder_path = os.path.join(args.output, basename)

        os.makedirs(folder_path)

        for intensity in brightness_intensities:
            filename = f"{basename}_brightness_{intensity:.1f}.jpg"
            
            attacked_image = brightness(img, intensity)
            attacked_image.save(os.path.join(folder_path, filename))

        for intensity in contrast_intensities:
            filename = f"{basename}_contrast_{intensity:.1f}.jpg"
            
            attacked_image = contrast(img, intensity)
            attacked_image.save(os.path.join(folder_path, filename))

        for intensity in gamma_intensities:
            filename = f"{basename}_illumination_{intensity:.2f}.jpg"
            
            attacked_image = gamma(img, intensity)
            attacked_image.save(os.path.join(folder_path, filename))

        for intensity in gaussian_intensities:
            filename = f"{basename}_gaussian_{intensity:.2f}.jpg"
            
            attacked_image = gaussian_noise(img, intensity)
            attacked_image.save(os.path.join(folder_path, filename))