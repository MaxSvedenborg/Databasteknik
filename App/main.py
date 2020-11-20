from DB import Base, engine, session
from Data.Models.cars import Car
from Data.Models.customers import Customer
from Data.Models.customertype import CustomerType

#add to Repository later
def main():
    customer_types = session.query(CustomerType).all()
    for customer_type in customer_types:
        print(customer_type)

    customers = session.query(Customer).all()
    for customer in customers:
        print(customer)

    cars = session.query(Car).all()
    for car in cars:
        print(car)


if __name__ == '__main__':
    main()
