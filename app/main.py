from db import Base, engine, session
from data.models.cars import Car

#add to repository later
def main():
    cars = session.query(Car).all()
    for car in cars:
        print(car)


if __name__ == '__main__':
    main()
