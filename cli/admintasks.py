import sqlite3

def write_customer_to_database(name, address, city, state, postal_code, telephone, active):
    '''write_customer_to_database, author: Jordan Nelson
    Creates a new customer in the database
    Method arguments
    ----------------
      name -- (text) The Customer's Name
      address -- (text) The Customer's Address
      city -- (text) The Customer's City
      state -- (text) The Customer's State
      postal_code -- (text) The Customer's Postal Code
      telephone -- (int) The Customer's Telephone
      active -- (bit) 0 (default) not active, 1 (active)
    '''
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (None, name, address, city, state, postal_code, telephone, active))

        conn.commit()

def get_customer_list():
    """purpose: get a list of customers
        author: casey dailey
        args: n/a
        return: list
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""select CustomerID, Name from Customer""")

        return c.fetchall()

def read_id_from_table(table_column, table_name, id_to_query):
    ''' read_id_from_table, author: Jordan Nelson
    Checks whether a specific ID exists in a table specified
    returns the ID specified if it exists or returns None if it does not
    Method arguments
    ----------------
      table_column -- the column in the table to query
      table_name -- the name of the table to run the query on
      id_to_query -- the specific id searched for
    '''
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT {} FROM {} WHERE {} = {} ORDER BY {} DESC LIMIT 1"""
            .format(table_column, table_name, table_column, id_to_query, table_column))

        result = c.fetchone()

        try:
            if result != None:
                return result[0]
            else:
                raise TypeError
        except TypeError:
            return None

def activate_customer(id):
    """
    Purpose: to set the boolean value of the selected customer to true
    Author: Harper Frankstone
    Args: id - (integer) the customer id, used to indicate which customer to set as active
    Return: n/a
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""update Customer set Active = {} where CustomerID is {}""".format(1, id))

        conn.commit()

def deactivate_customer(id):
    '''deactivate_customer, author: Jordan Nelson
    Sets the active flag to 0 (inactive)
    Method arguments
    ----------------
      id -- (int) The ID of the Customer to deactivate
    '''
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

def create_payment_type(payment_type_name, account_number, customer_id):
    '''create_payment_type, author: Aaron Barfoot
    Creates a new payment type in database and assign to active user
    ----------------
      payment_type_name -- (text) Name of payment type
      account_number -- (integer) Account number for payment type
      customer_id -- (integer) Customer ID of customer that added payment type
    '''
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO PaymentType VALUES (?, ?, ?, ?)",
            (None, payment_type_name, account_number, customer_id))

        conn.commit()

def get_payment_types(self, customer_id):
    ''' get_payment_types, author: Aaron Barfoot
    Returns the list of payment types assigned to the active user
    ----------------
      customer_id -- (integer) CustomerId to match with PaymentType.CutomerId
    '''
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT * FROM PaymentType WHERE {} = PaymentType.CustomerID"""
            .format(customer_id))

        paymenttypes = c.fetchall()
        try:
            if paymenttypes != None:
                return paymenttypes
            else:
                raise TypeError
        except TypeError:
            return None

def read_inventory():
    """ Query products, store as a list, and print to command line so customer can select a product to add to their order.

    Arguments: None.

    Author: James Tonkin """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("SELECT ProductID, ProductName FROM Product")
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

        return c.lastrowid

def get_customer_open_order(customer_id):
    """Purpose: query the database for a customer's open order
       Args: customer_id = a foreign key to the orders table
       Returns: the id of the order with
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""select OrderID
                    from Orders
                    where CustomerID = {}
                    and Orders.PaymentTypeID is null""".format(customer_id))

        customer_open_order = c.fetchone()

        return customer_open_order

def add_product_to_customer_order(product_id, order_id):
    """ Method to add products to a customer order.

    Arguments: product_id that was ordered, order_id that is the product is being added to.

    Author: James Tonkin """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO ProductOrder VALUES (?, ?, ?)",
                    (None, product_id, order_id))

        conn.commit()

def assign_payment_type_to_customer_order(order_id, payment_id):
    """Purpose: assigning a payment type to a customer's order will 'complete' the order
    Author: Casey Dailey
    Args: order_id=an integer, foreign key to the payment_type table specifies the order to be updated,
          payment_id=the value corresponding to a customer's particular payment type
    Returns: N/A
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

    c.execute("""update Orders
                 set PaymentTypeID = {}
                 where Orders.OrderID={};""".format(payment_id, order_id))

    conn.commit()

    return c.lastrowid

def read_top_three_products():
    """
    Purpose: to show the top three most purchased (popular) products
    Author: Harper Frankstone
    Args: n/a
    Return: a list containing strings of product names
    """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT Product.ProductName as Name,
                    Count(ProductOrder.ProductOrderID) as Purchased
                    FROM ProductOrder, Product
                    WHERE Product.ProductID = ProductOrder.ProductID
                    GROUP BY Product.ProductName
                    ORDER BY Purchased desc limit 3""")
        top_three = c.fetchall()
        return top_three
