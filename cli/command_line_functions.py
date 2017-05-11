from admintasks import *
from command_line_functions import *
from run import *

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

    try:
        user_input = int(input('> '))
        user_input = user_input - 1
        activate_customer(customers[user_input][0])
    except:
        print('Please choose a Customer from the list.')
        activate_a_customer_cli()

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
    if len(payment_type_name) < 1 or len(account_number) < 1:
        print("Please enter correct information.")
        pass
    if len(payment_type_name) > 1 and len(account_number) > 1:
    	create_payment_type(payment_type_name, account_number, customer_id)

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

    try:
        user_input = int(input('> '))

        if user_input < i + 1:
            selected_product_index = user_input - 1

            selected_product = inventory[selected_product_index]
            product_id = selected_product[0]

            add_product_to_customer_order(product_id, active_customer_open_order)
            add_product_to_cart_cli()
        elif user_input > i + 1:
            add_product_to_cart_cli()
        else:
            pass
    except:
        print("Please enter one of the numerical selections above.")
        add_product_to_cart_cli()

def complete_order_cli():
    """purpose: apply the user's chosen payment type to the active customer's open order
       author: casey dailey
       args: n/a
       returns: n/a
    """
    #in order to apply a payment type to a customer's order,
    #we need a customer_id and the order_id of that customer's open order
    customer_id = get_active_customer()
    open_order_id = get_customer_open_order(customer_id)

    #check for active customer. if none, prompt user to activate a customer.
    if customer_id == None:
        activate_a_customer_cli()

    #if active customer, go ahead
    else:

        #get the total price of all items in user's cart (open order)
        total = get_customer_order_total(customer_id)

        if total is None:
            input("Please add some products to your order first. Press any key to return to main menu. >")
            return

        print("Your order total is ${}.00. Ready to purchase?".format(total))
        choice = input("Y/N >")

        #case insensitive comparison to check for 'yes' input
        if choice.casefold() != 'y':
            return

        elif choice.casefold() == 'y':

            #get a list of tuples containing payment type(s)
            #information for active customer
            #iterate through the collection, print the name (index 1 of each tuple)
            #prepended with an integer (i) equal to the item's index plus 1 like this:
            # 1. Visa
            # 2. MasterCard
            payment_types = get_payment_types(customer_id)
            if payment_types:
                print("Select a payment option\n")
                i = 0
                for payment_type in payment_types:
                    i += 1
                    print('{}. {}'.format(i, payment_type[1]))

                #work back from the input to find the index of the selected payment type's id
                #pass that to assign_payment_type_to_customer_order method with the open_order_id
                try:
                    selection = int(input('>'))
                    selected_payment_type_index = selection - 1
                    x = payment_types[selected_payment_type_index]
                    selected_payment_type_id = x[0]
                    assign_payment_type_to_customer_order(open_order_id, selected_payment_type_id)

                    print("Your order is complete! Press any key to return to main menu.")
                    last_input = input(">")
                    if last_input != None:
                            return
                except:
                    print("Please enter one of the numerical selections above.")
                    complete_order_cli()
            else:
                print("You must create a payment type for this customer.")
                create_payment_option_cli()

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
