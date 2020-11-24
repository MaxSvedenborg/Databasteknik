import Data.Repository.customers_repo as cr


def get_all_customers():
    return cr.get_all_customers()


def get_customer_by_id(id):
    return cr.get_customer_by_id(id)


def get_customer_by_name(pattern):
    customers = cr.get_customer_by_name(pattern)
    return {i+1: customer for i, customer in enumerate(customers)}


def store_changes():
    cr.store_changes()


def store_new_name(customer, new_value):
    cr.store_new_name(customer, new_value)


def store_new_address(customer, new_value):
    cr.store_new_address(customer, new_value)


def store_new_phone(customer, new_value):
    cr.store_new_phone(customer, new_value)

def store_new_email(customer, new_value):
    cr.store_new_email(customer, new_value)

def store_new_customertype(customer, new_value):
    cr.store_new_customertype(customer, new_value)

#todo modify customer type