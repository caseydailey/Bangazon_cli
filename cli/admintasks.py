import sqlite3

def write_customer_to_database(self, name, address, city, state, postal_code, telephone):

    return 1 

def read_from_customer_table(self, table_name, property, id):

    return 1 

def activate_customer(self, id):
    """
    Purpose: to set the boolean value of the selected customer to true
    Author: Harper Frankstone
    Args: id - (integer) the customer id, used to indicate which customer to set as active 
    Return: n/a
    """
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()

        try:
           c.execute("""insert into customer [(active)] where customer_id is {} values {}""".format(id, 1))
        except sqlite3.OperationalError:
           pass

        conn.commit()

def get_active_customer(self):
    """
    Purpose: to show the active customer 
    Author: Harper Frankstone
    Args: n/a
    Return: the name of the active customer
    """

    with sqlite3.connect('db.db') as conn:
      c = conn.cursor()

      c.execute("select name from customer where active is {} order by customer_id desc limit 1".format(1))
      print(c.fetchone())


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

    pass

def  read_from_order_table(self, table_name, table_property, column_id):

    return 1 

def read_top_three_products(self):

    return ['Diaper']


