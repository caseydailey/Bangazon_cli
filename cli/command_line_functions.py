from admintasks import *
from command_line_functions import *
from run import *

"""
    ************** command_line_functions *****************
    This module serves as an intermediary relay between run.py and admintasks.py
    providing the methods to run.py that respond to the user's interaction with the 
    system and calling admintasks as needed. 

    methods: 
                create_customer_cli
                activate_customer_cli
                create_payment_option_cli
                add_product_to_cart_cli
                complete_order_cli
                product_popularity_cli
                view_cart_cli

"""

def create_customer_cli():
    """
    purpose: allow user to create a new customer account
    author: Jordan Nelson
    args: n/a
    returns: n/a
    helper methods: write_customer_to_database() from admintasks
    """
    name = input('Enter customer name:\n> ')
    address = input('Enter street address:\n> ')
    city = input('Enter city:\n> ')
    state = input('Enter state:\n> ')
    postal_code = input('Enter postal code:\n> ')
    phone_number = input('Enter phone number:\n> ')

    write_customer_to_database(name, address, city, state, postal_code, phone_number, active=0)

def activate_customer_cli():
    """
    purpose: check if customer is active or not and activate or not accordingly
    author: Jordan Nelson
    args: n/a
    returns: n/a
    helpers: get_active_customer, activate_a_customer_cli, deactivate_customer
    """
    active_customer = get_active_customer()

    """If a Customer is already active, deactivate the current customer
    then present the menu"""
    if active_customer == None:
        activate_a_customer_cli()
    else:
        deactivate_customer(active_customer)
        activate_a_customer_cli()

def activate_a_customer_cli():
    """
    purpose: allow user to activate a customer 
    author: Jordan Nelson
    args: n/a
    returns: n/a
    helpers: get_customer_list, activate_customer
    """
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
    """
    purpose: allow user to add a payment type to a customer account
    author: Aaron Barfoot
    args: n/a
    returns: n/a
    helpers: get_active_customer, create_payment_type
    """
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
    """ 
    purpose: allow user to add a product to an open order
    author: James Tonkin
    args: n/a
    returns: n/a
    helpers: 
    ---------------
        get_active_customer
        get_customer_open_order
        create_order
        read_inventory
        add_product_to_customer_order
    ---------------
    """
    #check for active customer
    active_customer = get_active_customer()

    if active_customer is None:
        print("Please select an active customer!")
        return
    active_customer_open_order_index = get_customer_open_order(active_customer)

    #if no order, create one
    if active_customer_open_order_index is None:
        active_customer_open_order = create_order(active_customer)
    else:
        active_customer_open_order = active_customer_open_order_index[0]

    #present user with a list of products
    # 1. candy
    # 2. cigs
    # 3. coffee
    # where the number corresponds to the products index in inventory + 1 (i + 1)
    # this creates a relationship between the user's input and the product's ID
    inventory = read_inventory()
    i = 0
    for prodid, prodname in inventory:
        i += 1
        print("{}. {}".format(i, prodname))
    print("{}. Done adding products".format(i + 1))

    #the user's input - 1 corresponds to the items index in inventory
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

def view_cart_cli():
    """
    purpose: view items in a customer's cart
    author: casey dailey
    args: n/a
    returns: n/a
    helpers: get_active_customer
    """
    active_customer = get_active_customer()
    #check if there's an active customer
    if active_customer:
        try:
            cart_info = view_products_in_customer_open_order(active_customer)
            cart_items = cart_info[0]
            item_names = [item[0] for item in cart_items]
            print("item in cart for customer {}: \n".format(active_customer))
            for index, item in enumerate(item_names):
                print("{}: {}".format(index + 1, item))
            print('Would you like to complete you order? y/n')
            answer = input('>')
            if answer == 'y':
                complete_order_cli()
            elif answer == 'n':
                return
            else: 
                print('please enter y or n')

        #check if there's an order
        except: 
            print('There are no items in your cart. would you like to create an order? y/n')
            response = input('>')
            if response == 'y':
                add_product_to_cart_cli()
            elif response == 'n':
                return
            else: 
                print('please enter y or n')

    else:
        print('please activate a customer')
        activate_customer_cli()

def complete_order_cli():
    """
    purpose: apply payment type to active customer's open order
    author: casey dailey
    args: n/a
    returns: n/a
    helpers: 
    -----------------
        get_active_customer
        get_customer_open_order
        activate_a_customer_cli
        get_customer_order_total
        get_payment_types
        assign_payment_type_to_customer_order
    -----------------
    """
    #in order to apply a payment type to a customer's order,
    #we need a customer_id and the order_id of that customer's open order
    customer_id = get_active_customer()
    try:
        open_order_id = get_customer_open_order(customer_id)
        if not open_order_id:
            create_order(customer_id)
    except:
        print('Please activate a Customer.')
        pass

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
    """
    purpose: show top three products
    author: Harper Frankstone
    args: n/a
    returns: n/a
    helpers: read_top_three_products
    prints a report that looks like this: 

        Product           Orders     Customers  Revenue
    *******************************************************
    Coffee            7          2             28
    Cigs              5          2             50
    Mug               4          2             20
    *******************************************************
    Totals:           16          6             $98

    """
    print('Product           Orders     Customers  Revenue        ')
    print('*******************************************************')

    top_three_products = read_top_three_products()

    # initalize variables for item data 
    total_products = 0
    total_orders = 0 
    total_customers = 0
    total_revenue = 0 

    # top_three_products = [('Coffee', 7, 2, 28), ('Cigs', 5, 2, 50), ('Mug', 4, 2, 20)]
    # count the number of characters in
    # name of product
    # how many times ordered
    # how many customers ordered product
    # total sales for product 
    for each in top_three_products:
        popular_product_character_count = len(each[0])
        order_count = len(str(each[1]))
        customer_count = len(str(each[2]))
        revenue_count = len(str(each[3]))

       #how many spaces to print to meet report format specifications
        product_column_spaces = 18 - popular_product_character_count
        order_column_spaces = 11 - order_count
        customer_column_spaces = 11 - customer_count
        revenue_column_spaces = 15 - revenue_count

        #vars for number of spaces to meet report format specifications
        s = ' ' * product_column_spaces
        o = ' ' * order_column_spaces
        c = ' ' * customer_column_spaces
        r = ' ' * revenue_column_spaces

        #convert integers to strings to make command line happy
        number_of_orders = str(each[1]) 
        customer_number = str(each[2])
        revenue_number = str(each[3])

        #print product_name + product_spaces, number_of_orders + order_spaces, revenue_spaces + revenue_number (amount) 
        print(each[0] + s + number_of_orders + o + customer_number + r + revenue_number)
        #gather orders, customers, and revenue totals for display below
        total_orders += each[1]
        total_customers += each[2]
        total_revenue += each[3]
        
    print('*******************************************************')
    print('Totals:           ' + str(total_orders) + '          ' + str(total_customers) + '             ' + '$' + str(total_revenue))
    print('')
    input('-> press return go back to the main menu')



