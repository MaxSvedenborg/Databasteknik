from Data.Models.customers import Customer
from DB import session

#todo
def get_all_customers():
    return session.query(Customer).all()


def get_customer_by_id(id):
    return session.query(Customer).filter(Customer.CustomerId == id).first()


def get_customer_by_name(pattern):
    return session.query(Customer).filter(Customer.CustomerName.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_name(customer, new_value):
    try:
        customer.CustomerName = new_value
        # ....
        session.commit()
    except:
        session.rollback()


def store_new_address(customer, new_value):
    try:
        customer.CustomerAddress = new_value
        # ....
        session.commit()
    except:
        session.rollback()


def store_new_phone(customer, new_value):
    try:
        customer.CustomerPhone = new_value
        # ....
        session.commit()
    except:
        session.rollback()

def store_new_email(customer, new_value):
    try:
        customer.CustomerEmail = new_value
        # ....
        session.commit()
    except:
        session.rollback()


def store_new_customertyp(customer, new_value):
    try:
        customer.CustomerType = new_value
        # ....
        session.commit()
    except:
        session.rollback()


def store_new_customertype(customer, new_value):
    return None