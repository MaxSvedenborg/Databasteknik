from Data.Models.stores import Store
from DB import session

def get_all_stores():
    return session.query(Store).all()


def create_new_stores():
    #add new stores into the Database system
    #As a user, I want to be able to add stores into the Database system.
    pass


def get_all_stores_by_customerId():
    #As a user, I want to be able to see which customers own this store.
    pass


def search_storesId():
    #As a user, I want to be able to search for storesID and see the details.
    pass
