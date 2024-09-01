from abc import ABC, abstractmethod
from image import Image

class Compressor(ABC):
    
    @abstractmethod
    def compressImage(self, image: Image):
        pass

class HighQualityCompressor(Compressor):

    def compressImage(self, image: Image):
        print(f"compressing image in good quality, {image.name}")

class LowQualityCompressor(Compressor):

    def compressImage(self, image: Image):
        print(f"compressing image in low quality, {image.name}")


class ModerateQualityCompressor(Compressor):

    def compressImage(self, image: Image):
        print(f"compressing image in decent quality, {image.name}")