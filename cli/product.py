import sys
import admintasks
import paymenttype
import order

class Product():
	
	def __init__(self, name, price):
		self.__name = name
		self.__price = price
		self.__product_id = None

	@property
	def name(self):
		return self.__name

	@property
	def price(self):
		return self.__price

	def save(self):
		self.__product_id = 1		



	
