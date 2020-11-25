import Data.Repository.ordersparepart_repo as osr

def get_all_orderspareparts():
    return osr.get_all_orderspareparts()


def get_ordersparepart_by_orderid(id):
    return osr.get_orderspareparts_by_orderid(id)


def store_changes():
    osr.store_changes()


def store_new_amount(ordersparepart, new_value):
    osr.store_new_amount(ordersparepart, new_value)


def store_new_ordersparepart(ordersparepart):
    osr.store_new_ordersparepart(ordersparepart)


def delete_ordersparepart(ordersparepart):
    osr.delete_ordersparepart(ordersparepart)