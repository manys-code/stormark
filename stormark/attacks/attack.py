"""
Image attack interface for all attacks.
"""
from abc import ABC, abstractmethod

class Attack(ABC):
    """
    Abstract attack class.
    """
    def __call__(self, img, intensity):
        return self.transform(img, intensity)

    @abstractmethod
    def transform(self, img, intensity):
        raise NotImplementedError

