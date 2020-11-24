from Data.Models.inventories import Inventories
from DB import session

def get_all_inventories():
    return session.query(Inventories).all()


def create_new_inventories():
    #add new cars into the Database system
    #As a user, I want to be able to add new cars into the Database system.
    pass


def get_all_inventories_by_customerId():
    #As a user, I want to be able to see which customers own this car.
    pass


def search_inventoriesId():
    #As a user, I want to be able to search for CarsID and see the details.
    pass
