class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.array = [None for i in range(capacity)]
            self.size = 0  # Track number of elements

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.getCapacity():
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
            value = self.array[self.size]
            self.array[self.size] = None
            return value

    def resize(self) -> None:
        self.array += [None] * len(self.array)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.array)