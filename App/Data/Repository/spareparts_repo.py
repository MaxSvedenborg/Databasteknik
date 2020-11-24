from Data.Models.spareparts import Sparepart
from DB import session

def get_all_spareparts():
    return session.query(Sparepart).all()


def create_new_spareparts():
    #add new cars into the Database system
    #As a user, I want to be able to add new cars into the Database system.
    pass


def get_all_cars_by_sparepartsId():
    #As a user, I want to be able to see which customers own this car.
    pass


def search_sparepartsId():
    #As a user, I want to be able to search for CarsID and see the details.
    pass