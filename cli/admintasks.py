import customer
import order
import product
import paymenttype

def read_customer_list(self):
    return ["Gerald"]

def activate_customer(self, customer):
    customer.active = True
    return customer

def add_product_to_customer_order(self, product, order):
    order.total = product.price
    return order

def read_inventory(self):
    return ["Dog"]

def select_order_payment_type(self, order, payment_type_id):
    order.payment_type_id = 1
    return order

