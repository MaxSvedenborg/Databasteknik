from UI.customers_menu import customers_menu
from UI.personaldata_menu import personal_data_menu
from UI.suppliers_menu import suppliers_menu


def main_menu():
    while True:
        print("Main Menu")
        print("=========")
        print("1. Customers")
        print("2. Customer Types")
        print("3. Cars")
        print("4. Orders")
        print("5. Personal Data")
        print("6. Employees")
        print("7. Cars Spareparts")
        print("8. Orders Spareparts")
        print("9. Suppliers")
        print("10. Stores")
        print("11. Manufacturer")
        print("12. Spareparts")
        print("13. Inventories")
        print("14. Quit")

        selection = input("> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            customers_type_menu()
        elif selection == "3":
            cars_menu()
        elif selection == "4":
            orders_menu()
        elif selection == "5":
            personal_data_menu()
        elif selection == "6":
            employees_menu()
        elif selection == "7":
            cars_spareparts_menu()
        elif selection == "8":
            orders_spareparts_menu()
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