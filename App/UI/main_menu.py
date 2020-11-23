from UI.customers_menu import customers_menu


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
        print("10. Store")
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

        else:
            break