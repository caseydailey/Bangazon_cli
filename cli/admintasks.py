import sqlite3
"""
    ************ admintasks.py ************

    This module contains core methods handling database interactions

    methods: 
                write_customer_to_database
                get_customer_list
                read_id_from_table
                activate_customer
                deactivate_customer
                get_active_customer
                create_payment_type
                get_payment_types
                read_inventory
                create_order
                add_product_to_customer_order
                assign_payment_type_to_customer_order
                read_top_three_products
"""
def write_customer_to_database(name, address, city, state, postal_code, telephone, active):
    """
    purpose: Creates a new customer in the database
    author: Jordan Nelson
    args:
    ----------------
      name -- (text) The Customer's Name
      address -- (text) The Customer's Address
      city -- (text) The Customer's City
      state -- (text) The Customer's State
      postal_code -- (text) The Customer's Postal Code
      telephone -- (int) The Customer's Telephone
      active -- (bit) 0 (default) not active, 1 (active)
    ----------------
    returns: n/a
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (None, name, address, city, state, postal_code, telephone, active))

        conn.commit()

def get_customer_list():
    """
    purpose: get a list of customers
    author: casey dailey
    args: n/a
    return: (list of tuples) ex: [(customer_id (integer), customer_name (string))] 
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT CustomerID, Name FROM Customer""")

        return c.fetchall()

def read_id_from_table(table_column, table_name, id_to_query):
    """ 
    purpose: Checks whether a specific ID exists in a table specified
    author: Jordan Nelson 
    args:
    ----------------
      table_column -- the column in the table to query
      table_name -- the name of the table to run the query on
      id_to_query -- the specific id searched for
    ---------------
    return: (int) ID specified if it exists or None
    """
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
    purpose: to set the boolean value of the selected customer to true
    author: Harper Frankstone
    args: id - (integer) the customer id. indicates which customer activate
    return: n/a
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""UPDATE Customer SET Active = {} WHERE CustomerID is {}""".format(1, id))

        conn.commit()

def deactivate_customer(id):
    """ 
    purpose: sets the active attribute to 0 (inactive)
    author: jordan nelson
    args: id -- (int) ID of the customer to deactivate
    returns: n/a    
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""UPDATE Customer SET Active = {} WHERE CustomerID is {}""".format(0, id))

        conn.commit()

def get_active_customer():
    """
    purpose: show active customer
    author: Harper Frankstone
    args: n/a
    returns: (int) ID of active customer
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT CustomerID FROM Customer WHERE Active is {} ORDER BY CustomerID DESC""".format(1))

        result = c.fetchone()
        try:
            if result != None:
                return result[0]
            else:
                raise TypeError
        except TypeError:
            return None

def create_payment_type(payment_type_name, account_number, customer_id):
    """
    purpose: Creates a new payment type in database and assign to active user
    author: Aaron Barfoot
    args:
    ----------------------
      payment_type_name -- (text) Name of payment type
      account_number -- (integer) Account number for payment type
      customer_id -- (integer) Customer ID of customer that added payment type
    ----------------------
    returns: n/a
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO PaymentType VALUES (?, ?, ?, ?)",
            (None, payment_type_name, account_number, customer_id))

        conn.commit()

def get_payment_types(customer_id):
    """
    purpose: 
    author: Aaron Barfoot
    args: customer_id -- (integer) Id of customer whose payment types we need to list
    returns: (list of tuples) 
        ex: [(2, 'visa', 1234567890123456, 1)] 
        where the above values represent:
        [(payment_type_id (integer), payment_type_name (string), account_number (integer), customer_id (integer))] 
    """
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
    """ 
    purpose: provide a list of available products
    author: James Tonkin 
    args: n/a
    returns: (list of tuples) 
        ex: [(2, 'cigs')] 
        where: [(2 is product_id (integer), 'cigs' is product_name (string))]
    """

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
    """ 
    purpose: creates a new order for a customer
    author: James Tonkin
    args: (integer) customer_id 
    returns: (integer) id of order created
    """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO Orders VALUES (?, ?, ?)",
                    (None, customer_id, None ))

        conn.commit()
        return c.lastrowid

def get_customer_open_order(customer_id):
    """
    purpose: get a customer's open order so they can add a product or complete
    author: Casey Dailey
    args: (integer) customer_id  whose open order we need
    returns: (tuple) containing OrderID ex: (7,)
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT OrderID
                     FROM Orders 
                     WHERE CustomerID = {}
                     AND PaymentTypeID is NULL""".format(customer_id))

        customer_open_order = c.fetchone()
        return customer_open_order

def get_customer_order_total(customer_id):
    """ 
    purpose: get total balance of a customer's order
    author: casey dailey
    args: (integer) id for customer whose order total we wish to see
    returns: (integer) total order balance
    """
    #get customer's open order id
    customer_open_order = get_customer_open_order(customer_id)
    customer_open_order_id = customer_open_order[0]

    #get sum of all products' prices on order
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT sum(Product.ProductPrice)
                               FROM ProductOrder, Product
                               WHERE ProductOrder.OrderID = {}
                               AND Product.ProductID = ProductOrder.ProductID""".format(customer_open_order_id))
    
    order_total = c.fetchone()
    return order_total[0]


def add_product_to_customer_order(product_id, order_id):
    """ 
    purpose: add products to a customer's order.
    author: James Tonkin
    args: (integer) product_id: product to add
          (integer) order_id: order to add to
    returns: n/a
    """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("INSERT INTO ProductOrder VALUES (?, ?, ?)",
                    (None, product_id, order_id))

        conn.commit()

def assign_payment_type_to_customer_order(order_id, payment_id):
    """
    purpose: assign a payment type to a customer's order to complete
    author: casey dailey
    args: (integer) order_id:  order to update
          (integer) payment_id:  payment type to apply
    returns: n/a 
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

    c.execute("""UPDATE Orders 
                 SET PaymentTypeID = {} 
                 WHERE OrderID = {}""".format(payment_id, order_id[0]))

    conn.commit()
    
def read_top_three_products():
    """
    purpose: to show the top three most purchased (popular) products
    author: Harper Frankstone
    args: n/a
    return: list of tuples 
        ex: [('Coffee', 7, 2, 28)]
        where: [(product_name (string), number_of_orders containing the product, number of customers who purchased the order, revenue from product)]
    """

    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT Product.ProductName as Name, 
                    Count(Distinct ProductOrder.ProductOrderID) as Purchased, 
                    Count(Distinct Orders.CustomerID) as Orders, 
                    Sum(Product.ProductPrice) as Revenue
                    FROM ProductOrder, Product, Orders
                    WHERE Product.ProductID = ProductOrder.ProductID
                    AND Orders.OrderID = ProductOrder.OrderID
                    GROUP BY Product.ProductName 
                    ORDER BY Purchased desc limit 3""")

        top_three = c.fetchall()
        return top_three

def read_order_contents(order_id):
    """
    purpose: to show the products in a customer's uncompleted order
    author: Harper Frankstone
    args: n/a
    return: list of tuples 
        ex: [('Coffee', 7, 2, 28)]
        where: [(product_name (string), the active customer's id, order_id, the product id)]
    """
    with sqlite3.connect('../db.db') as conn:
        c = conn.cursor()

        c.execute("""SELECT Product.ProductName, Customer.CustomerID, Orders.OrderID, Product.ProductID
            FROM Customer, Orders, Product
            WHERE Customer.CustomerID = Orders.CustomerID
            AND Customer.Active = 1 
            AND Orders.OrderID = {}
            AND Orders.PaymentTypeID ISNULL""".format(order_id))

        contents = c.fetchall()
        print(contents)
        try:
            if contents != None:
                return contents
            else:
                raise TypeError
        except TypeError:
            return None