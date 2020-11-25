from BL.carspareparts_controller import get_all_carspareparts, get_carsparepart_by_carid, store_new_carsparepart, \
    store_new_sparepartid, delete_carsparepart
from Data.Models.carspareparts import CarSparepart


def carspareparts_menu():
    while True:
        print("Carspareparts Menu")
        print("===========================")
        print("1. View All Carspareparts")
        print("2. View Carsparepart by Id")
        print("3. Find and Update Carsparepart")
        print("4. Create new Carsparepart into the system")
        print("5. Delete Carsparepart from the system")
        print("7. Exit Carspareparts Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            carspareparts = get_all_carspareparts()
            for carsparepart in carspareparts:
                print(carsparepart)

        elif selection == "2":
            id = input("Enter Car Id: ")
            carsparepart = get_carsparepart_by_carid(id)
            if carsparepart:
                print(carsparepart)
            else:
                print("Could not find carsparepart with carid ", id)

        elif selection == "3":
            id = input("Enter full or partial Car Id: ")
            carspareparts = get_carsparepart_by_carid(id)
            if len(carspareparts) > 0:
                for key, carsparepart in carspareparts.items():
                   print(f'{key}. {carsparepart}')

                edit_choice = input("Would you like to edit Carsparepart information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for Carsparepart to edit: ")
                    edit_selection = int(edit_selection)

                    carsparepart = carspareparts[edit_selection]
                    print(f'1. Customer Name: {carsparepart.SparepartId}')


                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new carsparepart Id: ")
                        store_new_sparepartid(carsparepart, new_value)
                        print("Sucessfully updated carsparepart Id")
            else:
                print("No Sparepart found")

        elif selection == "4":

            carsparepart = CarSparepart()
            carsparepart.CarsId = input("Enter Cars Id: ")
            carsparepart.SparepartId = input("Enter Sparepart Id: ")

            store_new_carsparepart(carsparepart)
            print("Sucessfully created new Carsparepart")

        elif selection == "5":
            id = input("Enter full or partial Cars Id: ")
            carspareparts = get_carsparepart_by_carid(id)
            if len(carspareparts) > 0:
                for key, carsparepart in carspareparts.items():
                    print(f'{key}. {carsparepart}')

                delete_selection = input("Enter number for Carsparepart Id to delete: ")
                delete_selection = int(delete_selection)

                carsparepart = carspareparts[delete_selection]
                delete_carsparepart(carsparepart)
                print("Sucessfully deleted customer")
        else:
            break
