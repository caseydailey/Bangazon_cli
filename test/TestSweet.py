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

    def test_user_can_view_products_in_customer_open_order(self):
        cart = admintasks.view_products_in_customer_open_order(1)#customer 1, order 1
        query_string = cart[1]

        self.assertEqual("""select Product.ProductName, Product.ProductPrice, Product.ProductID
                    from Orders, Product, ProductOrder 
                    where Orders.OrderID = {}
                    and ProductOrder.OrderID = Orders.OrderID
                    and ProductOrder.ProductID = Product.ProductID""", query_string)
