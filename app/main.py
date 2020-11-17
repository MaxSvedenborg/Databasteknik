from db import Base, engine, session
from data.models.cars import Car
from data.models.customers import Customer
from data.models.customer_type import CustomerType

#add to repository later
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
