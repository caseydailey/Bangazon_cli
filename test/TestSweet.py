import sys; sys.path.append('../cli/')
import unittest
import admintasks

class TestSweet(unittest.TestCase):


    def test_user_can_create_customer(self):
        # write_customer_to_database should return an id of the customer after writing to the database
        admintasks.write_customer_to_database(name="Casey", address="123 Easy St", city="Coolville", state="TN", postal_code=1234, telephone=1232345678, active=0)
        # the read_from_table takes the table name, the property to be read, and the row of the table to query
        saved_customer = admintasks.read_id_from_table(table_column='CustomerID', table_name='Customer', id_to_query=1)

        self.assertEqual(1, saved_customer)

    def test_user_can_activate_customer(self):
        # we are passing an id into the activate_customer method, which should set the active property of the customer who's id equals the customer id passed, as an argument, to true
        admintasks.activate_customer(id=1)
        # get_active_customer selects the customer id from the customer table where customer.active equals true
        active_customer = admintasks.get_active_customer()


        self.assertEqual(9, active_customer)

    def test_user_can_add_payment_type_to_customer_account(self):

        # create_payment_type will insert into the payment type table the values from the user's input, the '1' in the assertion is referring to the customer id 
        # admintasks.create_payment_type(self, payment_type_name='Visa', account_number=123456, customer_id=1)
        payment_type = admintasks.get_payment_types(self, customer_id=1)

        self.assertIn((1, 'Visa', 123456, 1), payment_type)


    def test_user_can_add_product_to_customer_order(self):
        # add_product_to_customer_order will add the product to the order table in the database
        productorder = admintasks.add_product_to_customer_order(1, 1)


        self.assertIsNotNone(productorder)


    def test_user_can_see_product_popularity(self):
        # this method queries the database for the most frequently purchased products from the ProductOrder table
        top_products = admintasks.read_top_three_products(self)


        self.assertIn('Diapers', top_products[0])
