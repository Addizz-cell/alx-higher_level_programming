#!/usr/bin/python3
"""
This module defines a Square class with private size attribute,
a getter, and a setter, and a public area method.
"""


class Square:
    """
    Represents a square with a private size attribute,
    a getter, a setter, and a public area method.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
