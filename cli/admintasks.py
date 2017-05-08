import sqlite3

def write_customer_to_database(self, name, address, city, state, postal_code, telephone):

    return 1 

def read_from_customer_table(self, table_name, property, id):

    return 1 

def activate_customer(id):
    """
    Purpose: to set the boolean value of the selected customer to true
    Author: Harper Frankstone
    Args: id - (integer) the customer id, used to indicate which customer to set as active 
    Return: n/a
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

       
        c.execute("""update Customer set Active = {} where CustomerID is {}""".format(0, id))
    
        conn.commit()

def get_active_customer():
    """
    Purpose: to show the active customer 
    Author: Harper Frankstone
    Args: n/a
    Return: the name of the active customer
    """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""select CustomerID from Customer where Active is {} order by CustomerID desc""".format(1))
      
        result = c.fetchone()
        try:
            if result != None:
                return result[0]
            else:
                raise TypeError
        except TypeError:
            return None

        conn.commit()



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


# if __name__ == '__main__':
#     activate_customer(3)
#     get_active_customer()