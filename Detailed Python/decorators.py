import time

def cacheResponse(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        cache[args] = func(*args, **kwargs)
        return cache[args]        
    return wrapper

@cacheResponse
def addNums(x: int, y: int):
    time.sleep(4)
    return x+y

print(addNums(2, 3))
print(addNums(2, 3))