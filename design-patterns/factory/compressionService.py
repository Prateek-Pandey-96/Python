from image import Image
from compressor import *

class CompressionService:

    def doCompression(self, image: Image, compressor: Compressor):
        compressor.compressImage(image)