import sys
import admintasks
import product
import paymenttype
import customer

class Order():
    
    def __init__(self, customer_id):
        self.__customer_id = customer_id
        self.__total = 0
        self.__payment_type_id = None
        self.__order_id = None

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def order_id(self):
        return self.__order_id

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, val):
        self.__total += val   

    @property
    def payment_type_id(self):
        return self.__payment_type_id   

    @payment_type_id.setter
    def payment_type_id(self, val):
        self.__payment_type_id = val

    def save(self):
        self.__order_id = 1     



    
