from admintasks import *
from command_line_functions import *

def create_customer_cli():

	name = input('Enter customer name:\n> ')
	address = input('Enter street address:\n> ')
	city = input('Enter city:\n> ')
	state = input('Enter state:\n> ')
	postal_code = input('Enter postal code:\n> ')
	phone_number = input('Enter phone number:\n> ')

	write_customer_to_database(name, address, city, state, postal_code, phone_number, active=0)
