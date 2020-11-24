from UI.cars_menu import cars_menu
from UI.customers_menu import customers_menu
from UI.customers_type_menu import customers_type_menu
from UI.orders_menu import orders_menu


def main_menu():
    while True:
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

        selection = input("> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            customers_type_menu()
        elif selection == "3":
            cars_menu()
        elif selection == "4":
            orders_menu()

        else:
            break