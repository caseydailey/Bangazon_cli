from admintasks import *
from command_line_functions import *

"""
    ************ run.py ********

    This Module serves as an interface between admintasks, command_line_functions, and the CLI
    It's purpose is to handle the user's interaction with the system by displaying menu options,
    gather the user's input and respond accordingly,
    calling the necessary methods in the command_line_functions methods.

"""

def build_menu():
    """
    purpose: Displays the initial menu to the user
    author: Jordan Nelson
    args: n/a
    returns: n/a
    """
    print('*********************************************************')
    print('**  Welcome to Bangazon! Command Line Ordering System  **')
    print('*********************************************************')
    print('1. Create a customer account')
    print('2. Choose active customer')
    print('3. Create a payment option')
    print('4. Add product to shopping cart')
    print('5. View products in active customer order')
    print('6. Add a product')
    print('7. Complete an order')
    print('8. See product popularity')
    print('9. Leave Bangazon!')

def start_program_menu():
    """
    purpose: Allows the user to select an option which calls
    author: Jordan Nelson
    args: n/a
    returns: n/a
    """
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
        view_active_customer_open_order_cli()

    if choice == '6':
        user_can_add_product_cli()

    if choice == '7':
        complete_order_cli()

    if choice == '8':
        product_popularity_cli()

    if choice == '9':
        active_customer = get_active_customer()
        deactivate_customer(active_customer)
        quit()

    start_program_menu()

if __name__ == '__main__':
	start_program_menu()
