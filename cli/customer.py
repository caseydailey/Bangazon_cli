import sys
import admintasks
import product
import paymenttype
import order

class Customer():
	
	def __init__(self, first_name, last_name):
		self.__first_name = first_name
		self.__last_name = last_name
		self.__customer_id = None

	@property
	def first_name(self):
		return self.__first_name

	@property
	def last_name(self):
		return self.__last_name

	def save(self):
		self.__customer_id = 1		



	
