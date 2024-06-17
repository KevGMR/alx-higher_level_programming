#!/usr/bin/python3
"""
Defines a square.

Attributes:
    - size (int): The size of the square.
"""
class Square:
	"""
	Initializes a new square instance.

	Parameters:
	- size (int, optional): The size of the square (default is 0).
	"""
	def __init__(self, size=0):
		self.size = size

	"""
	Getter method to retrieve the size of the square.

	Returns:
	- int: The size of the square.
	"""
	@property
	def size(self):
		return self.__size

	"""
	Setter method to set the size of the square.

	Parameters:
	- value (int): The new size of the square.

	Raises:
	- TypeError: If size is not an integer.
	- ValueError: If size is less than 0.
	"""
	@size.setter
	def size(self, value):
		if type(value) is not int:
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >=0")
		else:
			self.__size = value

	"""
	Calculates and returns the current square area.

	Returns:
	- int: The area of the square.
	"""
	def area(self):
		return self.__size ** 2

	"""
	Prints the square using the character #.

	If the size is equal to 0, print an empty line.
	"""
	def my_print(self):
		if self.__size == 0:
			print()
		else:
			for _ in range(self.__size):
				print("#" * self.__size)
