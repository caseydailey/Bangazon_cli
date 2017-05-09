from admintasks import *
from command_line_functions import *

def build_menu():
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
	build_menu()
	choice = input('> ')

	if choice == '1':
		create_customer_cli()

	if choice == '2':
		pass

	if choice == '3':
		pass

	if choice == '4':
		pass

	if choice == '5':
		pass

	if choice == '6':
		pass

	if choice != '7':
		start_program_menu()

if __name__ == '__main__':

	start_program_menu()