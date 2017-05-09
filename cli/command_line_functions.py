from admintasks import *
from command_line_functions import *

def create_customer_cli():
	'''create_customer_cli, author: Jordan Nelson
    Allows the user to input a customer's information which
    is then written to the database
    ----------------
	None
    '''
	name = input('Enter customer name:\n> ')
	address = input('Enter street address:\n> ')
	city = input('Enter city:\n> ')
	state = input('Enter state:\n> ')
	postal_code = input('Enter postal code:\n> ')
	phone_number = input('Enter phone number:\n> ')

	write_customer_to_database(name, address, city, state, postal_code, phone_number, active=0)

def activate_customer_cli():
	'''active_customer_cli, author: Jordan Nelson
	Calls the get_active_customer method. If anything other than 'None' is returned
	the user recieves a message that a customer is already active in the system.
    ----------------
	None
    '''
	active_customer = get_active_customer()

	if active_customer == None:
		activate_a_customer_cli()
	else:
		deactivate_customer(active_customer)
		activate_a_customer_cli()

def activate_a_customer_cli():
	'''activate_a_customer_cli, author: Jordan Nelson
	Presents the user with a list of all customers, by choosing the number of the
	customer, the specific customer is marked as active.
    ----------------
	None
    '''
	print('Which customer will be active?\n')

	customers =  get_customer_list()
	for custid, name in customers:
		print(str(custid) + '. ' + name)

	user_input = input('> ')
	user_input = int(user_input)

	for custid, name in customers:
		if user_input == custid:
			activate_customer(user_input)
			break

def create_payment_option_cli():
	'''create_payment_option_cli, author: Aaron Barfoot
	Allows user to add a payment type to their account and writes input to database
	-----------------
	None
	'''
	active_customer = get_active_customer()

	payment_type_name = input('Enter name of payment type:\n> ')
	account_number = input('Enter account number for payment type:\n> ')
	customer_id = active_customer

	create_payment_type(payment_type_name, account_number, customer_id)
	

def add_product_to_cart_cli():
	pass

def complete_order_cli():
	pass

def product_popularity_cli():
	pass