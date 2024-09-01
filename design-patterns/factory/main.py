from compressor import *

def takeInputAndGetCompressor(type: str) -> Compressor:
    type_map = {
       "low": LowQualityCompressor(),
       "high": HighQualityCompressor(),
       "medium": ModerateQualityCompressor()
    }
    
    if type in type_map:
        return type_map[type]
    return type_map["low"]

if  __name__ == '__main__':
    """
    We need to build an image compression system,
    there can be several algos that can be used.
    """
    type = input("enter a compression type: ")
    required_compressor = takeInputAndGetCompressor(type)
    required_compressor.compressImage(Image("image1", bytearray("imagedata", encoding="utf-8")))