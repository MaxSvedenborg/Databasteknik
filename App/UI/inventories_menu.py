from BL.stores_controller import get_all_inventories, get_inventory_by_id, store_new_inventory_location, \
    store_new_inventory_QTY, store_new_inventory_automatic_order, store_new_inventory, delete_inventory, \
    get_inventory_by_location, get_inventory_by_name
from Data.Models.inventories import Inventory


def inventories_menu():
    while True:
        print("Inventory Menu")
        print("===========================")
        print("1. View All Inventories")
        print("2. View inventories by Id")
        print("3. View Inventories by location")
        print("4. Find and Update Inventories")
        print("5. Create new inventories into the system")
        print("6. Delete inventories from the system")
        print("7. Exit Store Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            inventories = get_all_inventories()
            for Inventory in inventories:
                print(Inventory)

        elif selection == "2":
            id = input("Enter Inventory Id: ")
            Inventory = get_inventory_by_id(id)
            if Inventory:
                print(Inventory)
            else:
                print("Could not find inventory with id ", id)

        elif selection == "3":
            pattern = input("Enter full or partial name of the location of the inventory: ")
            inventories = get_inventory_by_location(pattern)

        elif selection == "4":
            pattern = input("Enter full or partial name of the inventory: ")
            inventories = get_inventory_by_name(pattern)
            if len(inventories) > 0:
                for key, Inventory in inventories.items():
                    print(f'{key}. {Inventory}')

                edit_choice = input("Would you like to edit inventory information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for inventory to edit: ")
                    edit_selection = int(edit_selection)

                    inventory = inventories[edit_selection]
                    print(f'1. Inventory location: {inventory.InventoryLocation}')
                    print(f'2. Inventory Amount: {inventory.InventoryQTY}')
                    print(f'3. Inventory Automatic order amount: {inventory.InventoryQTYAutomaticOrder}')


                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Inventory Location: ")
                        store_new_inventory_location(inventory, new_value)
                        print("Sucessfully updated new inventory location")
                    elif line == "2":
                        new_value = input("Enter new inventory Amount: ")
                        store_new_inventory_QTY(inventory, new_value)
                        print("Sucessfully updated new inventory amount")
                    elif line == "3":
                        new_value = input("Enter new amount for automatic order: ")
                        store_new_inventory_automatic_order(inventory, new_value)
                        print("Sucessfully updated new amount for automatic orders")

            else:
                print("No inventory found")


        elif selection == "5":
            inventory = Inventory()
            inventory.InventoryLocation = input("Enter InventoryLocation: ")
            inventory.InventoryQTY = input("Enter Inventory Amount: ")
            inventory.InventoryQTYAutomaticOrder = input("Enter Inventory automatic order amount: ")
            store_new_inventory(Inventory)
            print("Sucessfully created new inventory")

        elif selection == "6":
            pattern = input("Enter full or partial inventory name: ")
            stores = get_inventory_by_name(pattern)
            if len(inventories) > 0:
                for key, inventory in inventories.items():
                    print(f'{key}. {inventory}')

                delete_selection = input("Enter number for inventory to delete: ")
                delete_selection = int(delete_selection)

                inventory = inventories[delete_selection]
                delete_inventory(inventory)
                print("Sucessfully deleted inventory")

        else:
            break