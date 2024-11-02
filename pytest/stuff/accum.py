class Accumulator:

    def __init__(self):
        self.count = 0
    
    @property
    def count(self):
        return self.__count

    def add(self, more=1) -> None:
        self.__count += more