from admintasks import *
from command_line_functions import *
from run import *

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
	pass

def add_product_to_cart_cli():
	""" Gets active customer, then checks to see if customer has an open order. If no open order then will open a new order. Once an order is found or opened, pulls inventory of items and shows them to the user. User will select items to add to the shopping cart.
	Arguments: None
	Author: James Tonkin
	"""

	active_customer = get_active_customer()

	if active_customer is None:
		print("Please select an active customer!")
		return

	active_customer_open_order_index = get_customer_open_order(active_customer)

	if active_customer_open_order_index is None:
		active_customer_open_order = create_order(active_customer)
	else:
		active_customer_open_order = active_customer_open_order_index[0]

	inventory = read_inventory()
	i = 0
	for prodid, prodname in inventory:
		i += 1
		print("{}. {}".format(i, prodname))
	print("{}. Done adding products".format(i + 1))

	user_input = input('> ')
	if int(user_input) < i + 1:
		selected_product_index = int(user_input) - 1

		selected_product = inventory[selected_product_index]
		product_id = selected_product[0]

		add_product_to_customer_order(product_id, active_customer_open_order)
		add_product_to_cart_cli()
	else:
		pass

def complete_order_cli():
	pass

def product_popularity_cli():
	pass
