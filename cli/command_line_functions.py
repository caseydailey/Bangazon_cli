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
	"""Purpose: to show a table in the command line interface with the top three most popular products.
		Author: Harper Frankstone
		Requirements: 
		1)product column should be 18 characters long, and a max of 17 characters of the name should be shown
		2)the orders column should be 11 characters long
		3)the customers column should be 11 characters long
		4)the revenue column should be 15 characters long
		Args: None
	"""
	print('Product           Orders     Customers  Revenue        ')
	print('*******************************************************')
	top_three_products = read_top_three_products()
	# print(top_three_products)
	# I need to loop over the collection returned from read_top_three_products and take the strings of the product names, store in a variable. I should use the [] notation to select the first, second, and third products 
	# find a repeat method in python like the ng-repeat
	# do math to count the number of characters in a row in a column then subtract that length from the set number of characters allowed for the column
	total_products = 0
	total_orders = 0 
	total_customers = 0
	total_revenue = 0 
	for each in top_three_products:
		popular_product_character_count = len(each[0])
		order_count = len(str(each[1]))
		customer_count = len(str(each[2]))
		revenue_count = len(str(each[3]))

		product_column_spaces = 18 - popular_product_character_count
		order_column_spaces = 11 - order_count
		customer_column_spaces = 11 - customer_count
		revenue_column_spaces = 15 - revenue_count

		s = ' ' * product_column_spaces
		o = ' ' * order_column_spaces
		c = ' ' * customer_column_spaces
		r = ' ' * revenue_column_spaces

		number_of_orders = str(each[1]) 
		customer_number = str(each[2])
		revenue_number = str(each[3])

		print(each[0] + s + number_of_orders + o + customer_number + r + revenue_number)
		total_orders += each[1]
		total_customers += each[2]
		total_revenue += each[3]
		



	print('*******************************************************')
	print('Totals:           ' + str(total_orders) + '          ' + str(total_customers) + '             ' + '$' + str(total_revenue))
	print('')
	input('-> press return go back to the main menu')

	return 



