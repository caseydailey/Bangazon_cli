import sys
import admintasks
import product
import customer
import order

class PaymentType():
	
	def __init__(self, name, account_number, customer_id):
		self.__name = name
		self.__account_number = account_number
		self.__customer_id = customer_id
		self.__payment_type_id = None

	@property
	def name(self):
		return self.__name

	@property
	def account_number(self):
		return self.__account_number

	@property
	def customer_id(self):
		return self.__customer_id	

	@property
	def payment_type_id(self):
		return self.__payment_type_id	

	@payment_type_id.setter
	def payment_type_id(self, val):
		self.__payment_type_id = val

	def save(self):
		self.__payment_type_id = 1		
