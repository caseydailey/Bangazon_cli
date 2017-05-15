import sys; sys.path.append('../cli/')
import unittest
import admintasks

class TestSweet(unittest.TestCase):

    def test_user_can_create_customer(self):
        saved_customer = admintasks.read_id_from_table(table_column='CustomerID', table_name='Customer', id_to_query=1)
        self.assertEqual(1, saved_customer)

    def test_user_can_activate_customer(self):
        admintasks.activate_customer(id=1)
        active_customer = admintasks.get_active_customer()
        self.assertEqual(1, active_customer)
        admintasks.deactivate_customer(id=1)

    def test_user_can_add_payment_type_to_customer_account(self):
        payment_type = admintasks.get_payment_types(customer_id=1)
        self.assertIn((1, 'Discover', 12345678853, 1), payment_type) 

    def test_user_can_see_product_popularity(self):
        top_products = admintasks.read_top_three_products()
        self.assertIn('Car', top_products[0])
