import Data.Repository.employees_repo as er

def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(id):
    return er.get_employee_by_id(id)


def store_changes():
    er.store_changes()

def store_new_store(employee, new_value):
    er.store_new_store(employee, new_value)


def store_new_employee(employee):
    er.store_new_employee(employee)


def delete_employee(employee):
    er.delete_employee(employee)

