from DB import session
from Data.Models.storeemployees import StoreEmployee


def get_all_employees():
    return session.query(StoreEmployee).all()


def get_employee_by_id(id):
    return session.query(StoreEmployee).filter(StoreEmployee.StoreEmployeeId == id).first()


def store_changes():
    session.commit()


def store_new_store(storeemployee, new_value):
    try:
        storeemployee.StoreId = new_value
        session.commit()
    except:
        session.rollback()


def store_new_employee(storeemployee):
    try:
        session.add(storeemployee)
        session.commit()
    except:
        session.rollback()


def delete_employee(storeemployee):
    try:
        session.delete(storeemployee)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()