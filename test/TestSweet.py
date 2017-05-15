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

    def test_user_can_add_payment_type_to_customer_account(self):
        payment_type = admintasks.get_payment_types(customer_id=3)
        self.assertIn((1, 'Visa', 1111222233334444, 3), payment_type) 

    def test_user_can_see_product_popularity(self):
        top_products = admintasks.read_top_three_products()
        self.assertIn('Coffee', top_products[0])

# Please add an option in the menu titled "View customer order" that, when selected, will display any items that the customer has ordered, but not purchased yet (if any).

    def test_user_can_see_order_contents(self):
        """
        this test will test the contents of an order, and needs to test all components of the application that come prior to 
        """
        # the customer must be created before an order is 
        saved_customer = admintasks.read_id_from_table(table_column='CustomerID', table_name='Customer', id_to_query=1)

        self.assertEqual(1, saved_customer)

        # the customer must then be made active before the order can have products added to it
        admintasks.activate_customer(id=1)
        active_customer = admintasks.get_active_customer()

        self.assertEqual(1, active_customer)

        # once the customer is active, the user can add products to the order 
        admintasks.create_order(customer_id=1)
        admintasks.add_product_to_customer_order(product_id=1, order_id=1)

        # now that a product has been added to an order, a method is required to read the tuple or list of tuples that comes back from the sql query
        order_contents = admintasks.read_order_contents()

        self.assertIn('Coffee', order_contents[0])