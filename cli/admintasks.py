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

    pass

def  read_from_order_table(self, table_name, table_property, column_id):

    return 1 

def read_top_three_products(self):

    return ['Diaper']


