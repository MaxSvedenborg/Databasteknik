import Data.Repository.carspareparts_repo as csr

def get_all_carspareparts():
    return csr.get_all_carspareparts()


def get_carsparepart_by_carid(id):
    return csr.get_carsparepart_by_carid(id)


def store_changes():
    csr.store_changes()


def store_new_carid(carsparepart, new_value):
    csr.store_new_carid(carsparepart, new_value)


def store_new_sparepartid(carsparepart, new_value):
    csr.store_new_sparepartid(carsparepart, new_value)


def store_new_carsparepart(carsparepart):
    csr.store_new_carsparepart(carsparepart)


def delete_carsparepart(carsparepart):
    csr.delete_carsparepart(carsparepart)

