import sqlite3

def write_customer_to_database(self, name, address, city, state, postal_code, telephone):

    return 1 

def read_from_customer_table(self, table_name, property, id):

    return 1 

def activate_customer(self, id):

    return 1

def get_active_customer(self):

    return 1

def create_payment_type(self, payment_type_name, account_number, payment_type_id):

    return 1

def get_payment_types(self, customer_id):

    return 1 

def read_inventory(self):

    return ["Diapers"]

def add_product_to_customer_order(self, product, customer_id):

    pass 

def get_order(self, customer_id):

    return "Diapers"

def assign_payment_type_to_customer_order(self, order_id, payment_id):
    """Purpose: assigning a payment type to a customer's order will 'complete' the order
    Author: Casey Dailey
    Args: order_id=an integer, foreign key to the payment_type table specifies the order to be updated, 
          payment_id=the value corresponding to a customer's particular payment type
    Returns: N/A
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

    c.execute("""update order 
                 set payment_type_id={} 
                 where order_id={};""".format(payment_id, order_id))

    conn.commit()


def read_from_order_table(self, table_name, table_property, column_id):

    return 1 

def read_top_three_products(self):

    return ['Diaper']






