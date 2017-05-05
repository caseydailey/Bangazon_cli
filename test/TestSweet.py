import sys; sys.path.append('../cli/')
import unittest
import admintasks

class TestSweet(unittest.TestCase):


    def test_user_can_create_customer(self):
        # come back to these parameters later
        admintasks.write_customer_to_database(name, address, city, state, postal_code, telephone)
        saved_customer = admintasks.read_customer_from_database()

        self.assertEqual(1, saved_customer.id)


    def test_user_can_activate_customer(self):
        # we are passing an id into the activate_customer method, which should set the active property of the customer who's id equals the customer id passed, as an argument, to true
        admintasks.activate_customer(1)
        # get_active_customer selects the customer id from the customer table where customer.active equals true
        active_customer = admintasks.get_active_customer()

        self.assertEqual(active_customer, 1)

    def test_user_can_add_payment_type_to_customer_account(self):
        # create_payment_type will insert into the payment type table the values from the user's input, the '1' in the assertion is referring to the customer id 
        admintasks.create_payment_type('Visa', 123456, 1)
        payment_type = admintasks.get_payment_types()

        self.assertEqual(payment_type.id, 1) 

            
    def test_user_can_add_product_to_customer_order(self):
        # read_inventory will query the database for the list of products and print them to the command line. Inventory is a list of dictionaries, storing the where the product name is the key and the product's price is the value
        inventory = admintasks.read_inventory()
        product = inventory[0]
        # add_product_to_customer_order will add the product to the order table in the database 
        admintasks.add_product_to_customer_order(product)

        self.assertIsNotNone(inventory)



    # def test_user_can_complete_customer_order(self):
    #     admintasks.select_order_payment_type(self, self.order1, self.visa.payment_type_id)
    #     self.assertIsNotNone(self.order1.payment_type_id)





