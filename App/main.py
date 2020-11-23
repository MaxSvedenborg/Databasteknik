from Data.Repository.customertypes_repo import get_all_customertypes
from Data.Repository.customers_repo import get_all_customers
from Data.Repository.cars_repo import get_all_cars
from Data.Models.carspareparts import CarSparepart
from Data.Models.spareparts import Sparepart
from Data.Models.manufacturers import Manufacturer
from Data.Models.suppliers import Supplier
from Data.Models.personaldata import Personaldata
from Data.Models.inventories import Inventory
from Data.Models.orders import Order
from Data.Models.storeemployees import StoreEmployee
from Data.Models.stores import Store
from App.UI.main_menu import main_menu


def main():
    #print(StoreEmployee())
    #print(Order())
    #print(Inventory())
    #print(Store())
    #print(Personaldata())
    #print(Supplier())
    #print(Manufacturer())
    #print(Sparepart())
    #print(CarSparepart())

    #for customer_type in get_all_customertypes():
    #    print(customer_type)

    #for car in get_all_cars():
    #    print(car)

    #for customer in get_all_customers():
    #    print(customer)

    main_menu()


if __name__ == '__main__':
    main()
