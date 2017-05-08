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
    """ Query products, store as a list, and print to command line so customer can select a product to add to their order.

    Arguments: None.

    Author: James Tonkin """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("SELECT ProductName FROM Product")
        inventory = c.fetchall()

        try:
            if inventory != None:
                return inventory
            else:
                raise TypeError
        except TypeError:
            return None

def create_order(customer_id):
    """ Creates a new order.

    Arguments: customer_id that the order is for.

    Author: James Tonkin """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO Orders VALUES (?, ?, ?)",
                    (None, customer_id, None ))

        conn.commit()

def add_product_to_customer_order(product_id, order_id):
    """ Method to add products to a customer order.

    Arguments: product_id that was ordered, order_id that is the product is being added to.

    Author: James Tonkin """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO ProductOrder VALUES (?, ?, ?)",
                    (None, product_id, order_id))

        conn.commit()
        return c.lastrowid

def assign_payment_type_to_customer_order(self, order_id, payment_id):

    pass

def  read_from_order_table(self, table_name, table_property, column_id):

    return 1

def read_top_three_products(self):

    return ['Diaper']
