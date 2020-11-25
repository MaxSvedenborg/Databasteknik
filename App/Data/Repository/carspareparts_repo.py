from Data.Models.carspareparts import CarSparepart
from DB import session

def get_all_carspareparts():
    return session.query(CarSparepart).all()


def get_carsparepart_by_carid(id):
    return session.query(CarSparepart).filter(CarSparepart.CarsId == id).first()


def store_changes():
    session.commit()


def store_new_carid(carsparepart, new_value):
    try:
        carsparepart.CarsId = new_value
        session.commit()
    except:
        session.rollback()


def store_new_sparepartid(carsparepart, new_value):
    try:
        carsparepart.SparepartId = new_value
        session.commit()
    except:
        session.rollback()


def store_new_carsparepart(carsparepart):
    try:
        session.add(carsparepart)
        session.commit()
    except:
        session.rollback()


def delete_carsparepart(carsparepart):
    try:
        session.delete(carsparepart)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


