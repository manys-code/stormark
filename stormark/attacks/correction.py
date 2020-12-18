"""
Image correction algorithms
"""
import numpy as np

from PIL import Image, ImageEnhance
from skimage.exposure import adjust_gamma

from stormark.attacks import Attack


class BrightnessCorrection(Attack):
    """
    Brightness correction manipulation.
    """
    def __init__(self):
        pass

    def transform(self, img, intensity):
        brightness = ImageEnhance.Brightness(img)
        return brightness.enhance(intensity)

class ContrastCorrection(Attack):
    """
    Brightness correction manipulation.
    """
    def __init__(self):
        pass

    def transform(self, img, intensity):
        brightness = ImageEnhance.Contrast(img)
        return brightness.enhance(intensity)

class GammaCorrection(Attack):
    """
    Illumination correction through Gamma Correction
    """
    def __init__(self):
        pass
    def transform(self, img, intensity):
        image = np.array(img) / 255
        image = adjust_gamma(image, intensity)
        image = (image * 255).astype("uint8")
        return Image.fromarray(image)
