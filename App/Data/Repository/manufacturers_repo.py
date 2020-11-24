from Data.Models.manufacturers import Manufacturer
from DB import session

def get_all_manufacturers():
    return session.query(Manufacturer).all()


def create_new_manufacturers():
    #add new cars into the Database system
    #As a user, I want to be able to add new cars into the Database system.
    pass


def get_all_manufacturers_by_customerId():
    #As a user, I want to be able to see which customers own this car.
    pass


def search_manufacturersId():
    #As a user, I want to be able to search for CarsID and see the details.
    pass
