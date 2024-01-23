#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple)\
                or len(value) != 2 or not all(isinstance(i, int)\ 
                        for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        result = []
        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            result.append("\n")
        for _ in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)
        return "\n".join(result)


if __name__ == "__main__":
    Square = __import__('101-square').Square

    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
