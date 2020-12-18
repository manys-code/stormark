"""
Additive noise attacks
"""

import numpy as np

from PIL import Image
from skimage.util import random_noise

from stormark.attacks import Attack


class GaussianNoise(Attack):
    """
    Additive Gaussian noise
    """
    def __init__(self):
        pass

    def transform(self, img, intensity):
        image = np.array(img) / 255
        image = random_noise(image, mode="gaussian",  var=intensity**2)
        image = (image * 255).astype("uint8")
        return Image.fromarray(image)