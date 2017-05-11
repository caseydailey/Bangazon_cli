from admintasks import *
from command_line_functions import *

p = 0
def deactivate_on_startup():
	'''deactivate_on_startup, author: Jordan Nelson
    If a Customer is marked active on the initial program
    run, deactivate the customer
    Method arguments
    ----------------
	None
    '''
	global p
	if p == 0:
		active_customer = get_active_customer()

		if active_customer != None:
 			deactivate_customer(active_customer)
		p += 1

def build_menu():
    '''build_menu, author: Jordan Nelson
    Displays the initial menu to the user
    Method arguments
    ----------------
    None
    '''
    print('*********************************************************')
    print('**  Welcome to Bangazon! Command Line Ordering System  **')
    print('*********************************************************')
    print('1. Create a customer account')
    print('2. Choose active customer')
    print('3. Create a payment option')
    print('4. Add product to shopping cart')
    print('5. Complete an order')
    print('6. See product popularity')
    print('7. Leave Bangazon!')

def start_program_menu():
    '''start_program_menu, author: Jordan Nelson
    Allows the user to select an option which calls
    the specific method
    Method arguments
    ----------------
    None
    '''
    build_menu()
    choice = input('> ')

    if choice == '1':
        create_customer_cli()

    if choice == '2':
        activate_customer_cli()

    if choice == '3':
        create_payment_option_cli()

    if choice == '4':
        add_product_to_cart_cli()

    if choice == '5':
        complete_order_cli()

    if choice == '6':
        product_popularity_cli()

    if choice == '7':
        quit()

    start_program_menu()


if __name__ == '__main__':
	deactivate_on_startup()
	start_program_menu()

