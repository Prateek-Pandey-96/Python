class Cutter(object):
    def cut(self):
        print("cutting vegetables")

class Boiler(object):
    def boil(self):
        print("boiling vegetables")

class Frier(object):
    def fry(self):
        print("frying vegetables")

class Cook(object):
    def __init__(self, cutter, boiler, frier):
        self.cutter = cutter
        self.boiler = boiler
        self.frier = frier
    
    def prepare_dish(self):
        self.cutter.cut()
        self.boiler.boil()
        self.frier.fry()
        print("cooking dish")


if __name__ == "__main__":
    cook = Cook(Cutter(), Boiler(), Frier())
    cook.prepare_dish()