from BL.ordersparepart_controller import get_all_orderspareparts, get_ordersparepart_by_orderid, \
    store_new_ordersparepart, delete_ordersparepart, store_new_amount

from Data.Models.orderspareparts import OrderSparepart

def orderspareparts_menu():
    while True:
        print("Orderspareparts Menu")
        print("===========================")
        print("1. View All Orderspareparts")
        print("2. View Ordersparepart by Id")
        print("3. Find and Update Orderspareparts")
        print("4. Create new Ordersparepart into the system")
        print("5. Delete Ordersparepart from the system")
        print("7. Exit Orderspareparts Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            orderspareparts = get_all_orderspareparts()
            for ordersparepart in orderspareparts:
                print(ordersparepart)

        elif selection == "2":
            id = input("Enter Ordersparepart Id: ")
            ordersparepart = get_ordersparepart_by_orderid(id)
            if ordersparepart:
                print(ordersparepart)
            else:
                print("Could not find Ordersparepart with Order id ", id)

        elif selection == "3":
            id = input("Enter full or partial Order Id: ")
            orderspareparts = get_ordersparepart_by_orderid(id)
            if len(orderspareparts) > 0:
                for key, ordersparepart in orderspareparts.items():
                   print(f'{key}. {ordersparepart}')

                edit_choice = input("Would you like to edit Orderspareparts information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for customer to edit: ")
                    edit_selection = int(edit_selection)

                    ordersparepart = orderspareparts[edit_selection]
                    print(f'1. Orders Amount: {ordersparepart.OrderAmount}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Orders Amount: ")
                        store_new_amount(ordersparepart, new_value)
                        print("Sucessfully updated Orders Amount")
            else:
                print("No Order found")

        elif selection == "4":

            ordersparepart = OrderSparepart()
            ordersparepart.OrderId = input("Enter Order Id: ")
            ordersparepart.SparepartId = input("Enter Sparepart Id: ")
            ordersparepart.OrderAmount = input("Enter Order Amount: ")

            store_new_ordersparepart(ordersparepart)
            print("Sucessfully created Ordersparepart")

        elif selection == "5":
            id = input("Enter full or partial Ordersparepart Order Id: ")
            orderspareparts = get_ordersparepart_by_orderid(id)
            if len(orderspareparts) > 0:
                for key, ordersparepart in orderspareparts.items():
                    print(f'{key}. {ordersparepart}')

                delete_selection = input("Enter number for Ordersparepart to delete: ")
                delete_selection = int(delete_selection)

                ordersparepart = orderspareparts[delete_selection]
                delete_ordersparepart(ordersparepart)
                print("Sucessfully deleted Ordersparepart")
        else:
            break


