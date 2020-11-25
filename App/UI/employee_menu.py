from BL.employee_controller import get_employee_by_id, store_new_employee, delete_employee, get_all_employees
from Data.Models.storeemployees import StoreEmployee
from Data.Repository.employees_repo import store_new_store


def employee_menu():
    while True:
        print("Employees Menu")
        print("===========================")
        print("1. View All Employees")
        print("2. View Employees by Id")
        print("3. Find and Update Employees")
        print("4. Create new Employee into the system")
        print("5. Delete Employee from the system")
        print("7. Exit Employees Menu")

        selection = input("Please select options:  ")

        if selection == "1":
            employees = get_all_employees()
            for employee in employees:
                print(employee)

        elif selection == "2":
            id = input("Enter Employee Id: ")
            employee = get_employee_by_id(id)
            if employee:
                print(employee)
            else:
                print("Could not find Employee with id ", id)

        elif selection == "3":
            id = input("Enter full or partial Employee Id: ")
            employees = get_employee_by_id(id)
            if len(employees) > 0:
                for key, employee in employees.items():
                   print(f'{key}. {employee}')

                edit_choice = input("Do you want to edit Employee information [y/n]: ")
                if (edit_choice.lower() == "y"):
                    edit_selection = input("Enter number for Employee to edit: ")
                    edit_selection = int(edit_selection)

                    employee = employees[edit_selection]
                    print(f'1. Store Id: {employee.StoreId}')

                    line = input("Enter number for what line to edit: ")
                    if line == "1":
                        new_value = input("Enter new Store Id: ")
                        store_new_store(employee, new_value)
                        print("Sucessfully updated new Store Id")
            else:
                print("No Employee found")

        elif selection == "4":

            employee = StoreEmployee()
            employee.StoreId = input("Enter Store Id: ")
            employee.PersonalDataId = input("Enter Personal Data Id: ")

            store_new_employee(employee)
            print("Sucessfully created new Employee")

        elif selection == "5":
            id = input("Enter full or partial Employee name: ")
            employees = get_employee_by_id(id)
            if len(employees) > 0:
                for key, employee in employees.items():
                    print(f'{key}. {employee}')

                delete_selection = input("Enter number for Employee to delete: ")
                delete_selection = int(delete_selection)

                employee = employees[delete_selection]
                delete_employee(employee)
                print("Sucessfully deleted Employee")
        else:
            break
