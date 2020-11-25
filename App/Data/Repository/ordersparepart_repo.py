from Data.Models.orderspareparts import OrderSparepart
from DB import session


def get_all_orderspareparts():
    return session.query(OrderSparepart).all()


def get_orderspareparts_by_orderid(id):
    return session.query(OrderSparepart).filter(OrderSparepart.OrderId == id).first()


def store_changes():
    session.commit()


def store_new_amount(ordersparepart, new_value):
    try:
        ordersparepart.OrderAmount = new_value
        session.commit()
    except:
        session.rollback()


def store_new_ordersparepart(ordersparepart):
    try:
        session.add(ordersparepart)
        session.commit()
    except:
        session.rollback()


def delete_ordersparepart(ordersparepart):
    try:
        session.delete(ordersparepart)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()