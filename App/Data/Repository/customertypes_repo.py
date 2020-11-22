from Data.Models.customertypes import CustomerType
from DB import session


def get_all_customertypes():
    return session.query(CustomerType).all()
