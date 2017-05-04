import sys; sys.path.append('../cli/')

import unittest
from customer import Customer
from paymenttype import PaymentType
from order import Order
from product import Product
import admintasks

class TestSweet(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.gerald = Customer(first_name="Gerald", last_name="Krazinsky")
        self.gerald.save()

        self.visa = PaymentType(name="Visa", account_number=1, customer_id=1)
        self.visa.save()

        self.order1 = Order(customer_id=1)
        self.order1.save()
    
    def test_customer_has_first_name(self):
        self.assertEqual(self.gerald.first_name, "Gerald")

    def test_customer_has_last_name(self):
        self.assertEqual(self.gerald.last_name, "Krazinsky")

    def test_user_can_view_customer_list(self):
        customer_list = admintasks.read_customer_list(self)
        self.assertIn("Gerald", customer_list)  

    def test_user_can_activate_customer(self):
        admintasks.activate_customer(self, self.gerald)
        self.assertEqual(self.gerald.active, True)

    def test_user_can_add_payment_type_to_customer_account(self):
        self.assertEqual(self.visa.customer_id, 1)

    def test_user_can_read_product_list(self):
        inventory = []
        dog = Product(name="Dog", price=55.00)
        dog.save()
        inventory.append(dog)

        product_list = admintasks.read_inventory(self)
        self.assertIn("Dog", product_list)
            
    def test_user_can_add_product_to_customer_order(self):
        inventory = []
        dog = Product(name="Dog", price=55.00)
        dog.save()
        inventory.append(dog)

        admintasks.activate_customer(self, self.gerald)
        admintasks.add_product_to_customer_order(self, dog, self.order1)
        self.assertEqual(self.order1.total, dog.price)

    def test_user_can_complete_customer_order(self):
        admintasks.select_order_payment_type(self, self.order1, self.visa.payment_type_id)
        self.assertIsNotNone(self.order1.payment_type_id)





