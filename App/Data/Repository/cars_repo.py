from Data.Models.cars import Car
from DB import session

def get_all_cars():
    return session.query(Car).all()


def create_new_cars():
    #add new cars into the Database system
    #As a user, I want to be able to add new cars into the Database system.
    pass


def get_all_cars_by_customerId():
    #As a user, I want to be able to see which customers own this car.
    pass


def search_carsId():
    #As a user, I want to be able to search for CarsID and see the details.
    pass
