from admintasks import *
from command_line_functions import *

def create_customer_cli():
	'''create_customer_cli, author: Jordan Nelson
    Allows the user to input a customer's information which
    is then written to the database
    Method arguments
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
	Method arguments
    ----------------
	None
    '''
	active_customer = get_active_customer()

	'''If a Customer is already active, deactivate the current customer
	then present the menu'''
	if active_customer == None:
		activate_a_customer_cli()
	else:
		deactivate_customer(active_customer)
		activate_a_customer_cli()

def activate_a_customer_cli():
	'''activate_a_customer_cli, author: Jordan Nelson
	Presents the user with a list of all customers, by choosing the number of the
	customer, the specific customer is marked as active.
	Method arguments
    ----------------
	None
    '''
	print('Which customer will be active?\n')

	customers =  get_customer_list()

	i = 1
	for index in range(len(customers)):
		print(str(i) + '. ' + str(customers[index][1]))
		i += 1

	user_input = input('> ')
	user_input = int(user_input) - 1

	try:
		activate_customer(customers[user_input][0])
	except:
		print('Please choose a Customer from the list.')

def create_payment_option_cli():
	'''create_payment_option_cli, author: Aaron Barfoot
	Allows user to add a payment type to their account and writes input to database
	-----------------
	None
	'''
	active_customer = get_active_customer()

	if active_customer == None:
		print('You must select a customer to activate')
		activate_a_customer_cli()

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