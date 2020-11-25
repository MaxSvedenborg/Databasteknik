from UI.cars_menu import cars_menu
from UI.carspareparts_menu import carspareparts_menu
from UI.customers_menu import customers_menu
from UI.customers_type_menu import customers_type_menu
from UI.employees_menu import employees_menu
from UI.inventories_menu import inventories_menu
from UI.manufacturers_menu import manufacturers_menu
from UI.orders_menu import orders_menu
from UI.orderspareparts_menu import orderspareparts_menu
from UI.personaldata_menu import personaldata_menu
from UI.spareparts_menu import spareparts_menu
from UI.stores_menu import stores_menu
from UI.suppliers_menu import suppliers_menu


def main_menu():
    while True:
        print("=====================")
        print("Main Menu")
        print("=====================")
        print("1. Customers")
        print("2. Customer Types")
        print("3. Cars")
        print("4. Orders")
        print("5. Personal Data")
        print("6. Employees")
        print("7. Cars Spareparts")
        print("8. Orders Spareparts")
        print("9. Suppliers")
        print("10. Store")
        print("11. Manufacturer")
        print("12. Spareparts")
        print("13. Inventories")
        print("14. Exit")

        print("=====================")
        selection = input("Please enter option above >> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            customers_type_menu()
        elif selection == "3":
            cars_menu()
        elif selection == "4":
            orders_menu()
        elif selection == "5":
            personaldata_menu()
        elif selection == "6":
            employees_menu()
        elif selection == "7":
            carspareparts_menu()
        elif selection == "8":
            orderspareparts_menu()
        elif selection == "9":
            suppliers_menu()
        elif selection == "10":
            stores_menu()
        elif selection == "11":
            manufacturers_menu()
        elif selection == "12":
            spareparts_menu()
        elif selection == "13":
            inventories_menu()
        else:
            break
